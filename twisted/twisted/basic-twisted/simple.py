#! /usr/bin/env python
# coding=utf-8

import traceback
from twisted.internet import reactor


def stack():
    print('The python stack:')
    traceback.print_stack()


from twisted.internet import reactor

reactor.callWhenRunning(stack)
reactor.run()
