# Twisted学习笔记
### 1.Transports,Protocols,Protocol Factoies
- Transports
一个Twisted的Transport代表一个可以收发字节的单条连接。
- Protocols
一个具体的Twisted的Protocol的实现应该对应一个具体网络协议的实现，像FTP、IMAP或其它我们自己规定的协议。
每一个Twisted的Protocols类实例都为一个具体的连接提供协议解析。因此我们的程序每建立一条连接（对于服务方就是每接受一条连接），都需要一个协议实例。
- Protocol Factories
由于我们会将创建连接的工作交给Twisted来完成，Twisted需要一种方式来为一个新的连接制定一个合适的协议。制定协议就是Protocol Factories的 工作了。
Protocol Factory就是Factory模式的一个具体实现。buildProtocol方法在每次被调用时返回一个新Protocol实例。它就是Twisted用来为新连接创建新Protocol实例的方法。

### 2.在使用Twisted或其它基于reactor的异步编程体系时，都意味需要将我们的代码组织成一系列由reactor循环可以激活的回调函数链。

### 3.defer使用方法
- 在factory中创建deferred对象，但在调用factory对象之外返回自身的deferred对象，
然后再添加callback和errback
- 不显示创建deferred对象， 在函数返回时，我们调用defer.succeed(results)函数。
其中result则可以为调用我们延时操作函数返回的结果.

### 4.学习进度
[入门资料](https://www.gitbook.com/book/likebeta/twisted-intro-cn/details)
进度:1,2,3,4,5,6,7,8,9,10,11,12