#!/usr/bin/python3
#
# Created by Ian Howell on 12/20/17.
# File name: run.py
import argparse
from src import main

parser = argparse.ArgumentParser(description='A Tic-Tac-Toe AI')
x_help = "If set, the opponent will play as X's"
parser.add_argument('-x', '--is_x', action='store_true', help=x_help)
main.main(vars(parser.parse_args()))
