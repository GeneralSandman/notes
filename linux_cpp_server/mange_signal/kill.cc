#include <iostream>
#include <sys/types.h>
#include <signal.h>

int main(int argc,char ** argv){
    pid_t pid=pid_t(atoi(argv[1]));
    int sig=atoi(argv[2]);
    int res=kill(pid,sig);
    std::cout<<"send signal to "<<atoi(argv[1])<<std::endl;
    return 0;
}