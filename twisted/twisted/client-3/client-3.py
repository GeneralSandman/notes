#! /usr/bin/env python
# coding=utf-8

import optparse
import sys

from twisted.internet.protocol import Protocol, ClientFactory
from twisted.internet import reactor, defer


def parse_args():
    usage = """usage: %prog [options] [hostname]:port ...

This is the Get Poetry Now! client, Twisted version 3.0
Run it like this:

  python get-poetry-1.py port1 port2 port3 ...

If you are in the base directory of the twisted-intro package,
you could run it like this:

  python twisted-client-3/get-poetry-1.py 10001 10002 10003

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

    def connectionMade(self):
        print('connnect to:%s', self.transport.getHost())

    def dataReceived(self, data):
        self.poem += data
        msg = 'got %d bytes of poetry from %s'
        print(msg % (len(data), self.transport.getPeer()))

    def connectionLost(self, reason):
        print('connect lost from')
        self.factory.OnePoemFinished(self.poem)


class PoemClientFactory(ClientFactory):
    protocol = PoemClientProtocol

    def __init__(self, callback, errorback):
        self.callback = callback
        self.errorback = errorback

    def OnePoemFinished(self, poem):
        self.callback(poem)

    def clientConnectionFailed(self, connector, reason):
        print('connect failed')
        self.errorback(reason)


def main():
    adresss = parse_args()
    poems = []
    errors = []

    def OnePoemDone(poem):
        poems.append(poem)
        all_done()

    def PoemGetFailed(err):
        print >> sys.stderr, 'Poem failed:', err
        errors.append(err)
        all_done()

    def all_done():
        if len(poems) + len(errors) == len(adresss):
            print('success:%d--fail:%d' % (len(poems), len(errors)))
            reactor.stop()

    factory = PoemClientFactory(OnePoemDone, PoemGetFailed)

    for adress in adresss:
        host, port = adress
        reactor.connectTCP(host, port, factory)

    reactor.run()


if __name__ == '__main__':
    main()
