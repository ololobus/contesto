#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import yaml

from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application, url


def main():
    class MainHandler(RequestHandler):
        def get(self):
            self.write('Everithing is ok')


    app = Application([
        url(r'/', MainHandler),
    ])

    app.listen(sys.argv[1] if len(sys.argv) > 1 else 8888)
    IOLoop.current().start()

if __name__ == '__main__':
    main()
