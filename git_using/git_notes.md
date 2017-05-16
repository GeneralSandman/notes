1.git init
2.git add main.c
3.git commit -m "mm"
4.git status
5.git log --pretty=oneline
6.git reset --hard HEAD^1
7.git reset --hard ID号
8.git reflog # 查看历史git命令
9.前面讲了我们把文件往Git版本库里添加的时候，是分两步执行的：
第一步是用git add把文件添加进去，实际上就是把文件修改添加到暂存区；
第二步是用git commit提交更改，实际上就是把暂存区的所有内容提交到当前分支。
10.git diff HEAD -- main.c
	查看当前工作区和版本库的不同

11.http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/001374831943254ee90db11b13d4ba9a73b9047f4fb968d000
未明白
12.git checkout -- test.txt   将误删的文件从版本库恢复到工作区
13.git remote add origin git@github.com:GeneralSandman/learngit.git
	在本地库文件夹下，把本地库关联远程库
14.git config --global user.name "yourname"
git config --global user.email "youremail"
ssh-keygen -t rsa -C "13287069774@163.com"
