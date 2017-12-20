#!/usr/bin/python3
#
# Created by Ian Howell on 12/20/17.
# File name: test.py
from subprocess import Popen, PIPE

import itertools
import os
import time

bot_cmds = (['python3', '-u', 'run.py', '-x'], ['python3', '-u', 'run.py'])
bot1 = Popen(bot_cmds[0], stdout=PIPE, stdin=PIPE, bufsize=1,
             universal_newlines=True)
bot2 = Popen(bot_cmds[1], stdout=PIPE, stdin=PIPE, bufsize=1,
             universal_newlines=True)
bots = (bot1, bot2)

output_file = 'log.txt'
if os.path.isfile(output_file):
    os.remove(output_file)

for i in itertools.cycle([0, 1]):
    # Listen to bot i
    response = bots[i].stdout.readline().strip()

    # If bot i says we're done, stop
    if response == 'done':
        break

    with open(output_file, 'a') as f:
        f.write(str(response) + '\n')

    # Report back on what bot i said
    print("Bot {}: [{}]".format((i+1), response))
    time.sleep(1)

    # Tell the other bot what bot i said
    bots[i ^ 1].stdin.write(response + '\n')
