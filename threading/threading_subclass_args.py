#!/usr/bin/env python
# -*- coding: utf-8 -*-
# threading_subclass_args.py
# author: Kentaro Wada <www.kentaro.wada@gmail.com>

import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )

class MyThreadWithArgs(threading.Thread):
    def __init__(self, group=None, target=None, name=None,
            args=(), kwargs=None, verbose=None):
        threading.Thread.__init__(self, group=group, target=target,
                name=name, verbose=verbose)
        self.args = args
        self.kwargs = kwargs

    def run(self):
        logging.debug('running with %s and %s', self.args, self.kwargs)


for i in range(5):
    t = MyThreadWithArgs(args=(i,), kwargs={'a':'A', 'b':'B'})
    t.start()
