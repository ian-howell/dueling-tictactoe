#!/usr/bin/python3
#
# Created by Ian Howell on 12/20/17.
# File name: vis.py
from src import grid
import itertools
import os
import time

board = grid.Grid()
os.system('clear')
print(board)
time.sleep(1)
players = itertools.cycle(['X', 'O'])
with open('log.txt', 'r') as f:
    for line in f:
        pos = int(line)
        player = next(players)
        board.set(pos, player)
        os.system('clear')
        print(board)
        time.sleep(1)
