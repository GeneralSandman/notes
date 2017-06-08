#! /usr/bin/env python
# coding=utf-8
from twisted.internet import reactor, error, task
import time


def listen_tcp(portrange, host, factory):
    """Like reactor.listenTCP but tries different ports in a range."""
    assert len(portrange) <= 2, "invalid portrange: %s" % portrange
    if not hasattr(portrange, '__iter__'):
        return reactor.listenTCP(portrange, factory, interface=host)
    if not portrange:
        return reactor.listenTCP(0, factory, interface=host)
    if len(portrange) == 1:
        return reactor.listenTCP(portrange[0], factory, interface=host)
    for x in range(portrange[0], portrange[1] + 1):
        try:
            return reactor.listenTCP(x, factory, interface=host)
        except error.CannotListenError:
            if x == portrange[1]:
                raise


class CallLaterOnce(object):
    """Schedule a function to be called in the next reactor loop, but only if
    it hasn't been already scheduled since the last time it ran.
    """

    def __init__(self, func, *a, **kw):
        self._func = func
        self._a = a
        self._kw = kw
        self._call = None

    def schedule(self, delay=0):
        if self._call is None:
            self._call = reactor.callLater(delay, self)

    def cancel(self):
        if self._call:
            self._call.cancel()

    def __call__(self):
        self._call = None
        return self._func(*self._a, **self._kw)


class Slot(object):
    def __init__(self, nextcall):
        self.heatbeat = task.LoopingCall(nextcall.schedule)


def testCall():
    def next_spider(i):
        print("in function next_spider,get value:", i)

    # nextcall = CallLaterOnce(next_spider, 1)
    # heatbeat = task.LoopingCall(nextcall.schedule)
    # # nextcall.schedule()
    # heatbeat.start(1)
    # reactor.run()

    nextcall = task.LoopingCall(next_spider, 1)
    nextcall.start(1)
    reactor.run()


def testCls():
    class A(object):
        def __init__(self, name, score):
            self.name = name
            self.score = score

        @classmethod
        def getName(a):
            return a.name

        def getScore(a):
            return a.score

        @classmethod
        def returnSelf(cls):
            return cls

    a = A('li', 99)
    # print a.getName()
    # print a.getScore()

    # print A.getName
    # print A.getScore(a)
    # print a.getScore()
    # print A.returnSelf()
    # print type(A)
    # print type(a)


def testEngine():
    """Return a report of the current engine status"""

    def get_engine_status():
        """Return a report of the current engine status"""
        tests = [
            "time()-engine.start_time",
            "engine.has_capacity()",
            "len(engine.downloader.active)",
            "engine.scraper.is_idle()",
            "engine.spider.name",
            "engine.spider_is_idle(engine.spider)",
            "engine.slot.closing",
            "len(engine.slot.inprogress)",
            "len(engine.slot.scheduler.dqs or [])",
            "len(engine.slot.scheduler.mqs)",
            "len(engine.scraper.slot.queue)",
            "len(engine.scraper.slot.active)",
            "engine.scraper.slot.active_size",
            "engine.scraper.slot.itemproc_size",
            "engine.scraper.slot.needs_backout()",
        ]

        checks = []
        for test in tests:
            try:
                checks += [(test, eval(test))]
            except Exception as e:
                checks += [(test, "%s (exception)" % type(e).__name__)]

        return checks

    def format_engine_status():
        checks = get_engine_status()
        s = "Execution engine status\n\n"
        for test, result in checks:
            s += "%-47s : %s\n" % (test, result)
        s += "\n"

        return s

    def print_engine_status():
        print(format_engine_status())

    print_engine_status()


def testDisply():
    """
    pprint and pformat wrappers with colorization support
    """

    import sys
    from pprint import pformat as pformat_

    def _colorize(text, colorize=True):
        if not colorize or not sys.stdout.isatty():
            return text
        try:
            from pygments import highlight
            from pygments.formatters import TerminalFormatter
            from pygments.lexers import PythonLexer
            return highlight(text, PythonLexer(), TerminalFormatter())
        except ImportError:
            return text

    def pformat(obj, *args, **kwargs):
        return _colorize(pformat_(obj), kwargs.pop('colorize', True))

    def pprint(obj, *args, **kwargs):
        print(pformat(obj, *args, **kwargs))

    pprint('lizhenhu')


def testDeferList():
    from twisted.internet import defer
    def printResult(result):
        print(result)

    def addTen(result):
        return result + " ten"

    def addNine(result):
        return result + ' nine'

    def test1():
        # Deferred gets callback before DeferredList is created
        deferred1 = defer.Deferred()
        deferred2 = defer.Deferred()
        deferred1.addCallback(addTen)
        dl = defer.DeferredList([deferred1, deferred2])
        deferred2.addCallback(addNine)
        dl.addCallback(printResult)
        deferred1.callback("one")  # fires addTen, checks DeferredList, stores "one ten"
        deferred2.callback("two")
        # At this point, dl will fire its callback, printing:
        #     [(1, 'one ten'), (1, 'two')]

    def test2():
        # Deferred gets callback after DeferredList is created
        deferred1 = defer.Deferred()
        deferred2 = defer.Deferred()
        dl = defer.DeferredList([deferred1, deferred2])
        deferred1.addCallback(addTen)  # will run *after* DeferredList gets its value
        dl.addCallback(printResult)
        deferred1.callback("one")  # checks DeferredList, stores "one", fires addTen
        deferred2.callback("two")
        # At this point, dl will fire its callback, printing:
        #     [(1, 'one), (1, 'two')]

    test1()


def testReturnFun():
    def log_failure():
        def errback(failure):
            print(failure)

        return errback

    a = log_failure()
    a(3)


def testAd():
    import urllib
    import sys
    import re
    import json
    from bs4 import BeautifulSoup

    url = 'http://116.77.35.28/162.218.52.210/media/videos/mp4/10832.mp4?st=g_s4fDR5rFrWdOYo-Ktu8Q&e=1495982469'
    header = {
        'referer': 'http://www.1dav.com/api/read/zd.php?id=10832/黑丝制服装-售楼小姐的销售秘诀-叫的好浪&html5=1',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537\
                            .36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36',
    }
    response = urllib.urlretrieve(url, '1.mp4')


def testClass():
    class A(object):
        counter = 0

        def __init__(self, a, b):
            self.a = a
            self.b = b

        def __eq__(self, other):
            if self.a == other.a:
                return True
            else:
                return False

        def __setattr__(self, name, value):
            print('invoke function __setattr__')
            self.__dict__[name] = value + 1
            self.__dict__['counter'] += 1

    # a = A(1, 1)
    # print(a.a, a.b)
    # a.a = 2
    # a.b = 2
    # print(a.a, a.b)
    # print(a.counter)

    class AccessCounter(object):
        '''一个包含计数器的控制权限的类每当值被改变时计数器会加一'''
        counter = 0
        value = 0

        def __init__(self, val):
            super(AccessCounter, self).__setattr__('counter', 0)
            super(AccessCounter, self).__setattr__('value', val)
            print('invoke __init__()')

        def __setattr__(self, name, value):
            if name == 'value':
                super(AccessCounter, self).__setattr__('counter', self.counter + 1)
                # 如果你不想让其他属性被访问的话，那么可以抛出 AttributeError(name) 异常
            super(AccessCounter, self).__setattr__(name, value)
            print("invoke __setattr__()")
            del self.value

        def __delattr__(self, name):
            if name == 'value':
                super(AccessCounter, self).__setattr__('counter', self.counter + 1)
            super(AccessCounter, self).__delattr__(name)
            print('invoke __delattr__()')

        def __len__(self):
            return 22

    # a = AccessCounter(2)
    # print(a.counter)
    # a.value = 3
    # print(a.counter)
    # print(a.value)
    # print(len(a))

    class B(object):
        def __init__(self):
            self.d = {'a': 'aaa', 'b': 'bbb'}
            self.value = [1, 2, 3, 4, 5]

        def __getitem__(self, item):
            print('invoke __getitem__')
            return self.d[item]

        def __setitem__(self, key, value):
            print('invoke __setitem__')
            self.d[key] = value

        def __delitem__(self, key):
            print('invoke __delitem__')
            del self.d[key]

        def __iter__(self):
            print('invoke __iter__')
            return iter(self.value)

        def __contains__(self, item):
            print('invoke __contains__')
            return item in self.value

    b = B()
    print(b['a'])
    b['a'] = 'ooo'
    print(b['a'])
    del b['a']
    # print(b['a'])
    print('-----')
    iterr = iter(b)
    print(next(iterr))
    if 5 in b:
        print('error')
    else:
        print('true')


def testPrint(key, a):
    key = key % {'spider': a.name}
    print(key)


_loopCounter = 0
def testTask():
    from twisted.internet import task
    from twisted.internet import reactor

    loopTimes = 3
    failInTheEnd = True

    def runEverySecond():
        """
        Called at ever loop interval.
        """
        global _loopCounter

        if _loopCounter < loopTimes:
            _loopCounter += 1
            print('A new second has passed.')
            return

        if failInTheEnd:
            raise Exception('Failure during loop execution.')

        # We looped enough times.
        loop.stop()
        return

    def cbLoopDone(result):
        """
        Called when loop was stopped with success.
        """
        print("Loop done.")
        reactor.stop()

    def ebLoopFailed(failure):
        """
        Called when loop execution failed.
        """
        print(failure.getBriefTraceback())
        reactor.stop()

    loop = task.LoopingCall(runEverySecond)

    # Start looping every 1 second.
    loopDeferred = loop.start(1.0)

    # Add callbacks for stop and failure.
    loopDeferred.addCallback(cbLoopDone)
    loopDeferred.addErrback(ebLoopFailed)

    reactor.run()


if __name__ == "__main__":
    testTask()
