#!/usr/bin/python3
#
# Created by Ian Howell on 12/20/17.
# File name: main.py
from src import ai
from src import grid
import itertools


def main(args):
    # Initialize the board
    board = grid.Grid()

    player_symbols = itertools.cycle('XO')
    if args['is_x']:
        opponent = ai.AI('X')
        players = {'X': opponent.move, 'O': player_turn}
    else:
        opponent = ai.AI('O')
        players = {'O': opponent.move, 'X': player_turn}

    done = False
    turn = 0
    while not done:
        turn += 1
        player = next(player_symbols)
        pos = players[player](board)
        board.set(pos, player)

        winner = board.check_win()
        if winner or turn >= 9:
            done = True

    print('done')

    if args['is_x']:
        with open('results.txt', 'w') as f:
            f.write("{} wins!\n".format(winner))
            f.write(str(board) + '\n')


def player_turn(board):
    invalid = True
    while invalid:
        invalid = False
        pos = int(input())
        try:
            if board.at(pos) in 'XO':
                raise
        except:
            invalid = True
    return pos
