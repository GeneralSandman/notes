#! /usr/bin/env python
# coding=utf-8


import optparse, sys
from sys import stderr
from twisted.internet import defer
from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet import reactor, defer


def parse_args():
    usage = """usage: %prog [options] [hostname]:port ...

This is the Get Poetry Now! client, Twisted version 4.0
Run it like this:

  python get-poetry.py port1 port2 port3 ...

If you are in the base directory of the twisted-intro package,
you could run it like this:

  python twisted-client-4/get-poetry.py 10001 10002 10003

to grab poetry from servers on ports 10001, 10002, and 10003.

Of course, there need to be servers listening on those ports
for that to work.
"""

    parser = optparse.OptionParser(usage)

    _, addresses = parser.parse_args()

    if not addresses:
        print(parser.format_help())
        parser.exit()

    def parse_address(addr):
        if ':' not in addr:
            host = '127.0.0.1'
            port = addr
        else:
            host, port = addr.split(':', 1)

        if not port.isdigit():
            parser.error('Ports must be integers.')

        return host, int(port)

    return map(parse_address, addresses)


class PoemClientProtocol(Protocol):
    poem = ''

    def dataReceived(self, data):
        self.poem += data

    def connectionLost(self, reason):
        self.factory.poem_finished(self.poem)


class PoemClientFactory(ClientFactory):
    def __init__(self, d):
        self.defer = d

    def poem_finished(self, poem):
        self.defer.callback(poem)

    def clientConnectionFailed(self, connector, reason):
        self.defer.errback(reason)


def main():
    poems = []
    errors = []

    adresss = parse_args()

    def getPoemSuccess(poem):
        poems.append(poem)

    def getPoemFail(err):
        print >> stderr, 'failed:', err
        errors.append(err)

    def poem_done():
        if len(errors) + len(poems) == len(adresss):
            reactor.stop()


    d = defer.Defer()
    factory = PoemClientFactory(d)
    d.addCallBacks(getPoemSuccess,getPoemFail)
    d.addBoth(poem_done)

    for adress in adresss:
        host, port = adress
        reactor.connectTCP(host, port, factory)

    reactor.run()


if __name__ == '__main__':
    main()
