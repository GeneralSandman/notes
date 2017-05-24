#! /usr/bin/env python
# coding=utf-8


import optparse

from twisted.internet.protocol import ServerFactory
from twisted.protocols.basic import NetstringReceiver


def parse_args():
    usage = """usage: %prog [options]

This is the Poetry Transform Server.
Run it like this:

  python transformedpoetry.py

If you are in the base directory of the twisted-intro package,
you could run it like this:

  python twisted-server-1/transformedpoetry.py --port 11000

to provide poetry transformation on port 11000.
"""

    parser = optparse.OptionParser(usage)

    help = "The port to listen on. Default to a random available port."
    parser.add_option('--port', type='int', help=help)

    help = "The interface to listen on. Default is localhost."
    parser.add_option('--iface', help=help, default='localhost')

    options, args = parser.parse_args()

    if len(args) != 0:
        parser.error('Bad arguments.')

    return options


class TransformService(object):
    def transformLower(self, poem):
        return poem.lower()

    def transformUper(self, poem):
        return poem.upper()


class TransformServerProtocol(NetstringReceiver):
    def connectionMade(self):
        print ('one connection %s' % self.transport.getPeer())

    def stringReceived(self, string):
        if '.' not in string:
            self.sendString('form is error')
            self.transport.loseConnection()
            return

        xform_name, data = string.split('.', 1)
        self.xformRequest(xform_name, data)

    def xformRequest(self, xform_name, data):
        new_poem = self.factory.transformPoem(xform_name, data)

        if new_poem is not None:
            self.sendString(new_poem)

        self.transport.loseConnection()


class TransformServerFactory(ServerFactory):
    protocol = TransformServerProtocol

    def __init__(self, service):
        self.service = service

    def transformPoem(self, xform_name, poem):
        attr = getattr(self, ('xform_%s') % xform_name)

        if attr is None:
            return None

        try:
            return attr(poem)
        except:
            return None  # transform failed

    def xform_Lower(self, poem):
        return self.service.transformLower(poem)

    def xform_Upper(self, poem):
        return self.service.transformUper(poem)


def main():
    options = parse_args()

    service = TransformService()

    factory = TransformServerFactory(service)

    from twisted.internet import reactor

    port = reactor.listenTCP(options.port or 0, factory,
                             interface=options.iface)

    print 'Serving transforms on %s.' % (port.getHost(),)

    reactor.run()


if __name__ == '__main__':
    main()
