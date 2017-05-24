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
        print "in function next_spider,get value:", i

    # nextcall = CallLaterOnce(next_spider, 1)
    # heatbeat = task.LoopingCall(nextcall.schedule)
    # # nextcall.schedule()
    # heatbeat.start(1)
    # reactor.run()

    nextcall=task.LoopingCall(next_spider,1)
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

    print A.getName
    print A.getScore(a)
    print a.getScore()
    print A.returnSelf()
    print type(A)
    print type(a)


if __name__ == "__main__":
    testCall()
