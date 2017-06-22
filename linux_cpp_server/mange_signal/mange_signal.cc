#include <unistd.h>
#include <fcntl.h>
#include <sys/epoll.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>
#include <signal.h>
#include <iostream>
using namespace std;

static int pipefd[2];

int setnoblocking(int fd)
{
    int status = fcntl(fd, F_GETFD);
    int newstatus = status | O_NONBLOCK;
    if (fcntl(fd, F_SETFD, newstatus) == -1)
        cout << "error\n";
    return status;
}

int addfd(int epfd, int fd)
{
    epoll_event event;
    event.data.fd = fd;
    event.events = EPOLLIN | EPOLLET;
    int re = epoll_ctl(epfd, EPOLL_CTL_ADD, fd, &event);
    if (re == -1)
        cout << "epoll_ctl error\n";
    setnoblocking(fd);
}

void signal_handler(int sig)
{
    int old_error = errno;
    int msg = sig;
    send(pipefd[1], (char *)&sig, 1, 0);
    errno = old_error;
    cout<<"receive signal "<<sig<<endl;
}

void add_signal(int sign)
{
    struct sigaction sa;
    memset(&sa, 0, sizeof(sa));
    sa.sa_handler = signal_handler;
    sa.sa_flags |= SA_RESTART;
    sigfillset(&sa.sa_mask);
    int res = sigaction(sign, &sa, nullptr);
    if (res == -1)
        cout << "error\n";
}

int main(int argc, char **argv)
{
    cout<<"pid:"<<getpid()<<endl;
    const char *ip = argv[1];
    int port = atoi(argv[2]);

    struct sockaddr_in serv_addr;
    memset(&serv_addr, 0, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = inet_addr(ip);
    serv_addr.sin_port = htons(port);

    int listen_fd = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
    bind(listen_fd, (struct sockaddr *)&serv_addr, sizeof(serv_addr));
    listen(listen_fd, 8);

    int epfd = epoll_create(8);
    addfd(epfd, listen_fd);
    socketpair(PF_UNIX, SOCK_STREAM, 0, pipefd);
    setnoblocking(pipefd[1]);
    addfd(epfd, pipefd[0]);

    add_signal(SIGHUP);
    add_signal(SIGCHLD);
    add_signal(SIGTERM);
    add_signal(SIGINT);

    bool stop = false;

    struct epoll_event arrive_event[4];
    while (!stop)
    {
        int number = epoll_wait(epfd, arrive_event, 4, -1);

        for (int i = 0; i < number; i++)
        {

            int sockfd = arrive_event[i].data.fd;

            if (sockfd == listen_fd)
            {
                struct sockaddr_in client_addr;
                socklen_t client_addr_len = sizeof(client_addr);
                int conn_socket = accept(listen_fd, (struct sockaddr *)&client_addr,
                                         &client_addr_len);
                addfd(epfd, conn_socket);
            }

            else if ((sockfd == pipefd[0]) && (arrive_event[i].events & EPOLLIN))
            {
                int sig;
                char signals[1024];
                int ret = read(pipefd[0], signals, sizeof(signals));
                if (ret > 0)
                {
                    for (int i = 0; i < ret; i++)
                    {
                        switch (signals[i])
                        {
                        case SIGCHLD:
                        case SIGHUP:
                        {
                            continue;
                        }

                        case SIGTERM:
                        case SIGINT:
                        {
                            stop = true;
                        }
                        }
                    }
                }
            }
        }
    }

    close(listen_fd);
    close(pipefd[1]);
    close(pipefd[0]);

    return 0;
}
