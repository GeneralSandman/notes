#分布式爬虫学习笔记

```
应大数据的需求，分布式爬虫系统是解决这一问题的方案。分布式爬虫，对同一个网站的同类数据，进行结构化。同时，能利用分布式的软件设计方法，实现爬虫的高效采集。
```


- ### 电商网站具有以下特点：
1.数据变化极快，时效性极高
2.不同网站数据组织不同，分类标签不同
3.网站的反爬虫机制较强
4.每个页面被多个页面链接
- ### 重复链接多导致电商网站采集具有以下问题：
1.爬虫被反爬机制屏蔽
2.采集周期较长
3.需为不同的网站定制实现程序，进行结构化，人工成本较高
4.页面链接去重也影响采集效率


## 爬虫
1.爬虫策略
爬虫策略，应该保证爬虫的下载快速和高效，能解决爬虫面临的反爬虫问题。输入入口URL之后，自动分析网页的组织形态获取新的链接，进行下载。例如输入XX电商主页地址后，自动分析导航菜单，自动分析翻页地址，自动分析详情页的地址等。
2.URL去重算法
对URL进行去重，已经下载过的，没有进行数据更新的，不再进行下载。去重算法应考虑内存的问题，内存越小越优。
## 分布式调度算法
爬虫任务，可以理解为对一个网站的一次采集过程。
分布式爬虫将所有任务在多台机器上分布式执行（可用多进程模拟）。分布式调度策略，应该将不同网站的URL混合后，分配到多台机器上执行。分布式调度策略的重点在URL的分配策略、失败处理等。
分布式调度应该有多种调度策略，满足不同的场景需求。例如，有的任务必须在特定日期前执行完成，有的任务需要在另一个任务之后执行。
调度算法应该在满足特定的条件下，实现最大的下载量。
## 网页自动结构化
1.对于电商类网页，能对同一个网站的数据进行自动结构化，生成不同的表，例如商品表、店铺表、评价表等
2.对于新闻博客类网页，能进行网页正文的自动抽取，对正文进行自动摘要和关键词分析


## Python爬虫利器学习
- xpath分析网页利器
- Scrapy分布式爬虫框架
- scrapy-redis:基于redis的分布式爬虫框架，配合scrapy使用，让爬虫具有了分布式爬取的功能

## 分布式原理

[分布式原理博客](http://www.cnblogs.com/skying555/p/5021257.html)

## [使用scrapy,redis,mongodb实现的一个分布式网络爬虫](https://github.com/gnemoug/distribute_crawler/blob/master/woaidu_crawler/woaidu_crawler/commands/init_single_mongodb.py)
### 避免爬虫被禁的策略：
1.禁用cookie
2.实现了一个download middleware，不停的变user-aget
3.实现了一个可以访问google cache中的数据的download middleware(默认禁用)

### 调试策略的实现：
1.将系统log信息写到文件中
2.对重要的log信息(eg:drop item,success)采用彩色样式终端打印

### 爬虫状态查看：
1.将爬虫stats信息(请求个数，文件下载个数，图片下载个数等)保存到redis中
2.实现了一个针对分布式的stats collector，并将其结果用graphite以图表形式动态实时显示 





* * *
- install redis python api
```
sudo pip install redis
sudo pip install hiredis
```
- install mongo python api
```
sudo pip install pymong
```


* * *
## 自动获取网页结构化信息
[自动获取网页结构化信息的分析方法 ](https://www.google.com/patents/CN102750372A?cl=zh)

[利用自动规则生成的非结构化数据支持](http://google.si/patents/CN102779114A?cl=zh)





* * *
## 爬虫工具学习

1.Phantomjs
```
sudo apt-get install phantomjs
phantomjs --version
```


* * *
#### 1.如何获取js数据
	1.使用Python模拟
	2.Python执行JavaScript代码
python+gtk+pywebkit，相当于基于webkit自己写一个定制的浏览器

#### 2.scrapy不支持python3吗？有解决的办法吗？
```
pip install scrapy
不过可能会和原本python2的版本出现冲突，可执行文件直接覆盖。建议先备份/usr/local/bin目录下的scrapy的可执行文件，然后新生成的scrapy可执行文件命名为scrapy3这样scrapy命令执行的是python2的scrapyscrapy3执行的是python3的scrapy

sudo ln -s /usr/local/python3/bin/scrapy /usr/local/bin/scrapy3
```

#### 3.安装Graphite
[Ubuntu Server 14.04 x64安装Graphite](http://www.linuxdiyf.com/linux/21698.html)
[成功安装教程](http://note.axiaoxin.com/contents/install-and-use-graphite-on-ubuntu14.04.html)
[成功安装教程](https://graphite.readthedocs.io/en/latest/install-source.html)
[!!!!!!](https://jiamaoweilie.github.io/blog/2015/05/19/graphite/)
看安装脚本
[!!!!!!!!!](https://lanjingling.github.io/2016/04/04/graphite-1/)

#### 4.Graphite如何使用





