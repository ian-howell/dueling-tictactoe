#!/usr/bin/python3
#
# Created by Ian Howell on 12/20/17.
# File name: main.py
from src import ai
from src import grid
import itertools
import os


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

    output_file = 'log.txt'
    if os.path.isfile(output_file):
        os.remove(output_file)

    done = False
    turn = 0
    while not done:
        turn += 1
        player = next(player_symbols)

        if (not args['duel']):
            show_board(board)
            print("It is {}'s turn...".format(player))

        pos = players[player](board)
        board.set(pos, player)

        if (args['duel']) and (turn % 2 == args['is_x']):
            print(pos)

        if args['print']:
            with open(output_file, 'a') as f:
                f.write(str(pos) + '\n')

        winner = board.check_win()
        if winner or turn >= 9:
            done = True

    if (not args['duel']):
        show_board(board)
        if winner:
            print("{} wins!".format(winner))
        else:
            print("No one wins!")
    else:
        print('done')

    if args['print']:
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
            show_board(board)
            print("That's invalid. Try again")
            invalid = True
    return pos


def show_board(board):
    os.system("clear")
    print(board)
    print("*" * 10)
    print("HELP:")
    print(" 0 | 1 | 2 ")
    print("---+---+---")
    print(" 3 | 4 | 5 ")
    print("---+---+---")
    print(" 6 | 7 | 8 ")
