#!/usr/bin/python3
#
# Created by Ian Howell on 12/20/17.
# File name: test.py
from subprocess import Popen, PIPE

import itertools

bot_cmd1 = ['python3', '-u', 'run.py', '-xpd']
bot_cmd2 = ['python3', '-u', 'run.py', '-d']
bot1 = Popen(bot_cmd1, stdout=PIPE, stdin=PIPE, bufsize=1,
             universal_newlines=True)
bot2 = Popen(bot_cmd2, stdout=PIPE, stdin=PIPE, bufsize=1,
             universal_newlines=True)
bots = (bot1, bot2)

for i in itertools.cycle([0, 1]):
    # Listen to bot i
    response = bots[i].stdout.readline().strip()

    # If bot i says we're done, stop
    if response == 'done':
        break

    # Report back on what bot i said
    print("Bot {}: [{}]".format((i+1), response))

    # Tell the other bot what bot i said
    bots[i ^ 1].stdin.write(response + '\n')
