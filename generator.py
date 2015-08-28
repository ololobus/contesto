#!/usr/bin/env python

import sys
import os.path
import yaml

if os.path.isfile('config.yml'):
    sys.exit('App configuration already exists. Stopping...')

if len(sys.argv) < 3:
    sys.exit('Please, provide number of teams and tasks')
elif len(sys.argv) >= 3:
    teams_num = int(sys.argv[1])
    tasks_num = int(sys.argv[2])

# Making default configs
setup = {
    'teams': {},
    'tasks': {}
}

for tkn in range(1, tasks_num + 1, 1):
    setup['tasks'][tkn] = {
        'name': 'Task %s' % tkn,
        'description': '',
        'direction': 'ASC',
        'score_name': 'RMSE'
    }

for tmn in range(1, teams_num + 1, 1):
    setup['teams'][tmn] = {
        'name': 'Team %s' % tmn,
        'results': {}
    }
    for tkn in range(1, tasks_num + 1, 1):
        setup['teams'][tmn]['results'][tkn] = {
            'score': None,
            'details': ''
        }

# Writing config to yml
with open('config.yml', 'w') as outfile:
    outfile.write(yaml.dump(setup))
