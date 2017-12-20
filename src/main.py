#!/usr/bin/python3
#
# Created by Ian Howell on 12/20/17.
# File name: main.py
import grid
import random
import sys
import time


def main():
    board = grid.Grid()

    if len(sys.argv) == 1:
        player = 0
        player_sym = "XO"
    else:
        player = 1
        player_sym = "OX"
    for current_turn in range(9):
        board.print()
        print("*"*8)
        if player == 0:
            invalid = True
            while invalid:
                invalid = False
                pos = int(input(">>> "))
                try:
                    board.set(pos, player_sym[player])
                except:
                    print("But that's illegal...")
                    invalid = True

        else:
            random_nonsense()
            time.sleep(1)
            pos = board.get_random_valid()
            board.set(pos, player_sym[player])
        winner = board.check_win()
        if winner:
            break
        player ^= 1

    board.print()
    if winner:
        if winner == 'X':
            print("You got me!")
        else:
            print("I did it!")
    else:
        print("Looks like we tied...")


def random_nonsense():
    things = ("Good move!", "Hmm...", "I'm thinking", "You're on!",
              "Really?", "Rookie mistake...", "I'm gonna win!")
    print(random.sample(things, 1)[0])


if __name__ == "__main__":
    main()
