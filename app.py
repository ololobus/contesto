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

        teams = config['teams']
        tasks = config['tasks']

        for tkid in tasks.keys():
            task_teams = filter(lambda t: t['results'][tkid]['score'], list(teams.values()))
            task_teams = sorted(task_teams, key = lambda x: x['results'][tkid]['score'], reverse = orders[tasks[tkid]['direction']])

            tasks[tkid]['teams'] = zip(range(1, len(task_teams) + 1, 1), task_teams)

        self.render('contest.html', teams = teams, tasks = tasks)

def main():
    app = Application()

    app.listen(sys.argv[1] if len(sys.argv) > 1 else 8888)
    IOLoop.current().start()

if __name__ == '__main__':
    main()
