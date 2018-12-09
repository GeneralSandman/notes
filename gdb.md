# gdb教程

1.编译时指定-g
```
g++ -std=c++11 -g -o a test.cc
```
2.使用gdb调试
```
gdb a
```
3.gdb命令

|命令|功能|
|-|-|
|l|列出源代码|
|回车|重复上一次命令|
|b|设置断点|
|r|运行|
|n|单条语句执行,不进入函数|
|c|继续运行至下一断点|
|p|打印变量|
|bt|查看函数堆栈|
|s|step,进入函数|
|finish|退出函数|


4.查看断点信息
```
info break
```

5.设置断点
```
break 16
break func
```

6.用gdb同时调试一个运行程序和core文件，core是程序非法执行后core dump后产生的文件
```
gdb <program> core
```


7.指定这个服务程序运行时的进程ID
```
gdb <program> <PID>
```

8.常用的启动参数

```
    -symbols <file> 
    -s <file> 
    从指定文件中读取符号表。

    -se file
    从指定文件中读取符号表信息，并把他用在可执行文件中。

    -core <file>
    -c <file> 
    调试时core dump的core文件。

    -directory <directory>
    -d <directory>
```

9.如何调用一个函数```func```

```
call func()
或
print func()
```

10.退出正在调试的函数

```
finish
```

11.打印堆栈信息

```backtrace``` 简称 ```bt```

```info frame```





---
> ### 1.多线程调试
- 查看当前进程的线程。
```
info threads
```
- 切换调试的线程为指定ID的线程。
```
thread <PID>
```
- 在file.c文件第100行处为所有经过这里的线程设置断点。
```
break file.c:100 thread all
```

- 在线程中执行命令
```
thread apply <id1> <1d2> <command>
thread apply all <command>
```

- step或者c会使整个程序的所有线程向前执行,若想要只调试当前线程
```
set scheduler-locking off|on|step

off :不锁定任何线程，也就是所有线程都执行，这是默认值.
on:只有当前被调试程序会执行.
step:在单步的时候，除了next过一个函数的情况以外，只有当前线程会执行
```

> ### 2.调试宏

编译时指定 --ggdb3
```
g++ -std=c++11 -ggdb3 -o a test.cc
```
运行gdb时
```
info macro <AAA>
```

> ### 3.条件断点
```
b <where> if <condion>
```

> ### 4.设置,查看命令行参数
```
set args <args>
show args
```

> ### 5.x命令

16进制/16进制无符号/十进制/字符/字符串
```
x/<x/u/d/c/s> <addr>
```

- x/x <addr> 16进制显示


> ### 6.切换查看工作目录

```
cd <path>
pwd
```