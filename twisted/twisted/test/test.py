#! /usr/bin/env python
# coding=utf-8


from twisted.internet import reactor, defer


def testBasic():
    def getDummyData(inputData):
        """
        This function is a dummy which simulates a delayed result and
        returns a Deferred which will fire with that result. Don't try too
        hard to understand this.
        """
        print('getDummyData called')
        deferred = defer.Deferred()
        # simulate a delayed result by asking the reactor to fire the
        # Deferred in 2 seconds time with the result inputData * 3
        reactor.callLater(0, deferred.callback, inputData * 3)
        return deferred

    def cbPrintData(result):
        """
        Data handling function to be added as a callback: handles the
        data by printing the result
        """
        print('Result received: {}'.format(result))

    deferred = getDummyData(3)
    deferred.addCallback(cbPrintData)

    # manually set up the end of the process by asking the reactor to
    # stop itself in 4 seconds time
    reactor.callLater(9, reactor.stop)
    # start up the Twisted reactor (event loop handler) manually
    print('Starting the reactor')
    reactor.run()
    print('stop the reactor')


def testMore():
    class Getter:
        def gotResults(self, x):
            if self.d is None:
                print("Nowhere to put results")
                return

            d = self.d
            self.d = None
            if x % 2 == 0:
                d.callback(x * 3)
            else:
                d.errback(ValueError("You used an odd number!"))

        def _toHTML(self, r):
            """
        This function converts r to HTML.

        It is added to the callback chain by getDummyData in
        order to demonstrate how a callback passes its own result
        to the next callback
        """

            return "Result: %s" % r

        def getDummyData(self, x):
            """
        The Deferred mechanism allows for chained callbacks.
        In this example, the output of gotResults is first
        passed through _toHTML on its way to printData.

        Again this function is a dummy, simulating a delayed result
        using callLater, rather than using a real asynchronous
        setup.
        """
            self.d = defer.Deferred()
            # simulate a delayed result by asking the reactor to schedule
            # gotResults in 2 seconds time
            reactor.callLater(2, self.gotResults, x)
            # reactor.callLater(3, self.gotResults, x)
            self.d.addCallback(self._toHTML)
            return self.d

    def cbPrintData(result):
        print(result)

    def ebPrintError(failure):
        import sys
        sys.stderr.write(str(failure))

    # this series of callbacks and errbacks will print an error message
    g = Getter()
    d = g.getDummyData(3)
    d.addCallback(cbPrintData)
    d.addErrback(ebPrintError)

    d = g.getDummyData(4)
    d.addCallback(cbPrintData)
    d.addErrback(ebPrintError)

    # # this series of callbacks and errbacks will print "Result: 12"
    # g = Getter()
    # d = g.getDummyData(4)
    # d.addCallback(cbPrintData)
    # d.addErrback(ebPrintError)

    reactor.callLater(4, reactor.stop)
    reactor.run()


def testMyself():
    class Spider(object):
        def getInfomation(self, x):
            self.d = defer.Deferred()
            reactor.callLater(2, self.getResponse, x)
            self.d.addCallback(self.toHtml)
            return self.d

        def getResponse(self, x):
            if x % 2 == 0:
                self.d.callback(x * 3)
            else:
                self.d.errback(ValueError("You used an odd number!"))

        def toHtml(self, r):
            print('get html information ', r)
            return 'lizhenhu'

    def cbPrintData(result):
        print(result)

    def ebPrintError(failure):
        import sys
        sys.stderr.write(str(failure))

    s = Spider()
    d = s.getInfomation(2)
    d.addCallback(cbPrintData)
    d.addErrback(ebPrintError)

    reactor.callLater(4, reactor.stop)
    reactor.run()


def testDistribute():
    class aException(Exception):
        pass

    class bException(Exception):
        pass

    class cException(Exception):
        pass

    class dException(Exception):
        pass

    def startEngineFailed():
        print('start engine failed')

    def startEngine(x):
        d = defer.Deferred()
        d.addCallback(startCrawler)
        d.addErrback(startEngineFailed)

        if x<=8:
            print('start engine succ')
        else:
            raise aException

        return d

    def startCrawler(x):
        if x <= 7:
            print('start crawler successfully')
            return x
        else:
            raise aException

    def getDownloader(x):
        if x <= 6:
            print('download successfully')
            return x
        else:
            raise bException

    def parser(x):
        if x <= 5:
            print('parser succ')
            return x
        else:
            raise cException

    def store(x):
        if x <= 4:
            print('store succ')
            return x
        else:
            raise dException


    def cbPrintData(result):
        print(result)

    def ebPrintError(failure):
        import sys
        sys.stderr.write(str(failure))

    d = startEngine(7)
    d.addCallback(cbPrintData)
    d.addErrback(ebPrintError)

    reactor.callLater(9, reactor.stop)
    reactor.run()


if __name__ == "__main__":
    testMore()
