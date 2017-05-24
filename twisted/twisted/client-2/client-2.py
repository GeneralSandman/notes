#! /usr/bin/env python
# coding=utf-8

import optparse
from twisted.internet import reactor, defer
from twisted.internet.protocol import Protocol, ClientFactory


def parse_args():
    usage = """usage: %prog [options] [hostname]:port ...

This is the Get Poetry Now! client, Twisted version 2.0.
Run it like this:

  python get-poetry.py port1 port2 port3 ...

If you are in the base directory of the twisted-intro package,
you could run it like this:

  python twisted-client-2/get-poetry.py 10001 10002 10003

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


class PoetryProtocol(Protocol):
    poem = ''
    task_num = 0

    def dataReceived(self, data):
        self.poem += data
        msg = 'Task %d: got %d bytes of poetry from %s'
        print(msg % (self.task_num, len(data), self.transport.getPeer()))

    def connectionLost(self, reason):
        self.poemReceived(self.poem)

    def poemReceived(self, poem):
        self.factory.OnePoemFinish(self.task_num, poem)


class PoemFactory(ClientFactory):
    protocol = PoetryProtocol
    connect_num = 0

    def __init__(self, server_number):
        self.server_number = int(server_number)
        self.poems = {}
        self.connect_num = 0

    def buildProtocol(self, addr):
        protocol = ClientFactory.buildProtocol(self, addr)
        self.connect_num += 1
        protocol.task_num = self.connect_num
        return protocol

    def OnePoemFinish(self, poem=None, task_num=None):
        if poem is not None:
            self.poems[task_num] = poem
        self.connect_num -= 1

        if self.connect_num == 0:
            reactor.stop()

    def startedConnecting(self, connector):
        print('factory start to warking')

    def clientConnectionLost(self, connector, reason):
        print('connect lost:')
        self.OnePoemFinish()

    def clientConnectionFailed(self, connector, reason):
        print('connect failed:')
        self.OnePoemFinish()


def main():
    adresss = parse_args()
    server_number = len(adresss)
    factory = PoemFactory(server_number)

    for adress in adresss:
        host, port = adress
        reactor.connectTCP(host, port, factory)
    reactor.run()


if __name__ == '__main__':
    main()
