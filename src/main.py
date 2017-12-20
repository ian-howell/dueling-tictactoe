#!/usr/bin/python3
#
# Created by Ian Howell on 12/20/17.
# File name: main.py
import grid


def main():
    board = grid.Grid()
    board.print()
    board.set(0, 2, 'x')
    board.print()


if __name__ == "__main__":
    main()
