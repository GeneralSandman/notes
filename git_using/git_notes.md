1.初始化仓库
```
git init
```
2.添加文件
```
git add <filename>
```
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
### 15.gi

1. 创建分支
```
git branch dev
```
2.切换分支
```
git checkout dev
```
3.查看分支
```
git branch
```
4.合并dev分支到当前分支
```
git merge dev
```
5.删除分支（如果分支代码未提交，则删除失败）
```
git branch -d dev
```
6.当Git无法自动合并分支时，就必须首先解决冲突。解决冲突后，再提交，合并完成。
7.图示分支状况
```
git log --graph --pretty=oneline
```
8.准备合并dev分支，请注意--no-ff参数，表示禁用Fast forward
```
git merge --no-ff -m "merge with no ff" dev
```
9.当前工作现场“储藏”起来，等以后恢复现场后继续工作
```
git stash
```
10.恢复现场并删除stash
```
git stash apply
git stash drop
```
或
```
git stash pop
```
11.查看隐藏的工作区
```
git stash list
```
12.修复bug时，我们会通过创建新的bug分支进行修复，然后合并，最后删除；
当手头工作没有完成时，先把工作现场git stash一下，然后去修复bug，修复后，再git stash pop，回到工作现场。
13.创建分支并切换分支
```
git checkout -b feature-vulcan
```
14.强制删除分支，并抛弃分支的所有内容
```
git branch -D dev
```
15.查看远程库信息
```
git remote -v
```
16.合并本地库推送到远程库的master分支
```
git push origin master
```
17.[多人协作模式](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013760174128707b935b0be6fc4fc6ace66c4f15618f8d000)
18.添加标签
```
git tag v1.0
```
19.为标签指定commit ID
```
git tag v0.0 7dccc
```
20.查看标签
```
git tag
```
21.为标签指定附加信息
```
git tag -a <tagname> -m "blablabla..."
```
22.删除标签
```
git tag -d <tagname>
```
23.推送某个标签到远程
```
git push origin <tagname>
```
24.推送全部标签到远程
```
git push origin --tags
```
25.删除远程标签
```
git push origin :refs/tags/<tagname>
```
26.[忽略特殊文件](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/0013758404317281e54b6f5375640abbb11e67be4cd49e0000)