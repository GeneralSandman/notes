#! /usr/bin/env python
# coding=utf-8

from twisted.internet.protocol import ClientFactory
from twisted.protocols.basic import NetstringReceiver
from twisted.internet import reactor, defer
import optparse


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


class PoemClientProtocol(NetstringReceiver):
    def connectionMade(self):
        self.sendString('Upper.aaa')

    def stringReceived(self, string):
        print(string)

    def OnePoemDone(self):
        self.factory.poem_finished()


class PoemClientFactory(ClientFactory):
    protocol = PoemClientProtocol

    def __init__(self, d):
        self.defer = d

    def poem_finished(self, poem):
        if self.deferred is not None:
            d, self.deferred = self.deferred, None
            d.callback(poem)

    def clientConnectionFailed(self, connector, reason):
        if self.deferred is not None:
            d, self.deferred = self.deferred, None
            d.errback(reason)

def getPoem(host, port):
    d = defer.Deferred()
    factory = PoemClientFactory(d)
    reactor.connectTCP(host, port, factory)
    return d


def main():
    addresss = parse_args()

    for address in addresss:
        host, port = address
        d = getPoem(host, port)

    reactor.run()


if __name__ == '__main__':
    main()
