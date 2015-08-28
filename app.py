#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import yaml
import operator
import tornado.web

from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, url

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            url(r'/', MainHandler)
        ]
        settings = {
            'template_path': 'views',
            'static_path': 'assets'
        }
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(RequestHandler):
    def get(self):
        config = yaml.load(open('config.yml', 'r'))
        orders = { 'ASC': False, 'DESC': True }
        # self.write('Everithing is ok')
        teams = config['teams']
        tasks = config['tasks']
        for tkid in tasks.keys():
            tasks[tkid]['teams'] = sorted(list(teams.values()), key = lambda x: x['results'][tkid]['score'], reverse = orders[tasks[tkid]['direction']])

        self.render('contest.html', teams = teams, tasks = tasks)

def main():
    app = Application()

    app.listen(sys.argv[1] if len(sys.argv) > 1 else 8888)
    IOLoop.current().start()

if __name__ == '__main__':
    main()
