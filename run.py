#!/usr/bin/python3
#
# Created by Ian Howell on 12/20/17.
# File name: run.py
import argparse
from src import main

parser = argparse.ArgumentParser(description='A Tic-Tac-Toe AI')

x_help = "If set, the opponent will play as X's"
parser.add_argument('-x', '--is_x', action='store_true', help=x_help)

results_help = "If set, log the game to log.txt and the results to results.txt"
parser.add_argument('-p', '--print', action='store_true', help=results_help)

duel_help = "Only used in duel.py"
parser.add_argument('-d', '--duel', action='store_true', help=duel_help)

main.main(vars(parser.parse_args()))
