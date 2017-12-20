#!/usr/bin/python3
#
# Created by Ian Howell on 12/20/17.
# File name: test.py
from subprocess import Popen, PIPE
import time


bot_cmds = (['python3', '-u', 'run.py', '-x'], ['python3', '-u', 'run.py'])
bot1 = Popen(bot_cmds[0], stdout=PIPE, stdin=PIPE, bufsize=1,
             universal_newlines=True)
bot2 = Popen(bot_cmds[1], stdout=PIPE, stdin=PIPE, bufsize=1,
             universal_newlines=True)
bots = (bot1, bot2)

response = bot1.stdout.readline().strip()
print("1 says '{}'".format(response))
time.sleep(1)

while response != 'done':
    bot2.stdin.write(response + '\n')
    bot2.stdin.flush()
    response = bot2.stdout.readline().strip()
    print("2 says '{}'".format(response))
    time.sleep(1)

    bot1.stdin.write(response + '\n')
    bot1.stdin.flush()
    response = bot1.stdout.readline().strip()
    print("1 says '{}'".format(response))
    time.sleep(1)
