## Scrpay源码分析

### 1.crawl命令最终会执行CrawlProcess的crawl和start方法(scrapy/commends/crawl.py中的run()函数)(CrawlProcess位于scrapy/crawler.py)

### 2.scrapy/crawler.py中Class Crawler的crawl方法修饰为defer.inlineCallbacks,表明如果阻塞则放弃执行权.

### 3.defer.DeferredList函数(待学习) task.Cooperator()(scrapy/utils/defer.py 中parallel函数用于同时处理多条数据)   chainDeferred函数(待学习)

### 4.一个CrawlProcess可以控制多个Crawler来同时进行多个爬取任务，CrawlProcess通过调用Crawler的crawl方法来进行爬取，并通过_active活动集合跟踪所有的Crawler.

### 5.crawler会创建spider,创建engine

### 6.依赖注入

### 7.engine根据配置加载调度器模块,下载器模块,刮取器模块(主要处理下载后的结果和解析数据)

### 8.engine使用open_spider() 定时爬取

### 9.scrapy/crawler.py CrawlProcess中的start掌控者整体的开始运行

### 10.logging.root.removeHandler函数

### 11.os.path的join函数

### 12.scheduler模块最为难理解,用于控制Request对象的存储和获取，并提供了过滤重复Request的功能。另外还有一个LOG_UNSERIALIZABLE_REQUESTS参数，它是用来指定如果一个请求序列化失败，是否要记录日志。

### 13.Scraper的主要作用是对网络蜘蛛中间件进行管理，通过中间件完成请求，响应，数据分析等工作。中间件管理器MiddlewareManager

### 14.ExecutionEngine在open_spider里会调用scraper的open_spider方法来初始化scraper

### 15.引擎里会通过不断执行’_next_request'方法来处理新的请求，其中又会在不需要backout时调用'_next_request_from_scheduler'来处理新请求

### 16.网络蜘蛛中间件管理器的scrape_response方法,这个方法首先依次调用中间件的'process_spider_input'方法，然后调用传递进来的scrap_func，也就是call_spider方法，如果某个中间件的'process_spider_input'方法抛出了异常，则以Failure调用call_spider方法。如果所有中间件都处理成功，且call_spider也返回成功，则调用'process_spider_output'方法，这个方法依次调用中间件的'process_spider_output'方法

### 17.Downloader _download方法首先将request加入slot的inprogress集合记录正在进行的request,然后调用下载器downloader的fetch方法，给fetch返回的deferred添加一个'_on_success'方法，这样在下载完成后会打印日志并发送一个response_received消息给关心者。

### 18.对于同一个域名的访问策略可以通过slots获取而不用每次都解析配置。根据key从slots里取对应的Slot对象，如果还没有，则构造一个新的对象.

### 19.Downloader的fetch函数调用中间件管理器的download方法，同时传入了自己的_enqueue_request方法。


### 17.downloer中的slotSlot对象的字典，key是request对应的域名，值是一个Slot对象.lot对象用来控制一种Request下载请求，通常这种下载请求是对于同一个域名。这个Slot对象还控制了访问这个域名的并发度，下载延迟控制，随机延时等，主要是为了控制对一个域名的访问策略，一定程度上避免流量过大被封IP，不能继续爬取。