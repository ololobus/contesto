#!/usr/bin/env python

import sys
import ast
import os.path
import yaml
import subprocess

if not os.path.isfile('config.yml'):
    sys.exit('App configuration doesn\'t exist. Stopping...')

if len(sys.argv) < 3:
    sys.exit('Please, provide team_id and task_id')
elif len(sys.argv) >= 3:
    tmid = int(sys.argv[1])
    tkid = int(sys.argv[2])

proc = subprocess.Popen(['python', 'data_providers/%s.py' % tkid,  str(tmid)], stdout = subprocess.PIPE, stderr = subprocess.PIPE)
output = proc.communicate()

if output[0] != '':
    config = yaml.load(open('config.yml', 'r'))
    config['teams'][tmid]['results'][tkid] = ast.literal_eval(output[0])

    with open('config.yml', 'w') as outfile:
        outfile.write(yaml.dump(config))
else:
    print 'Error rised, update failed!\n-----\n', output[1]


