#!/usr/bin/python3
#
# Created by Ian Howell on 12/20/17.
# File name: main.py
import grid


def main():
    board = grid.Grid()

    player = 0
    player_sym = "XO"
    for current_turn in range(9):
        board.print()
        pos = int(input("Player {}:".format(player+1)))
        board.set(pos, player_sym[player])

        winner = board.check_win()
        if winner:
            print("Player {} wins".format(winner))
            break

        player ^= 1

    board.print()


if __name__ == "__main__":
    main()
