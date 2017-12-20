#!/usr/bin/python3
#
# Created by Ian Howell on 12/20/17.
# File name: main.py
import grid


def main():
    board = grid.Grid()
    winning_boards = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6))

    player = 0
    player_sym = "XO"
    for current_turn in range(9):
        board.print()
        pos = int(input("Player {}:".format(player+1)))
        board.set(pos, player_sym[player])
        player ^= 1

    board.print()


if __name__ == "__main__":
    main()
