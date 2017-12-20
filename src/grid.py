#!/usr/bin/python3
#
# Created by Ian Howell on 12/20/17.
# File name: grid.py
import random


class Grid:
    def __init__(self, size=3):
        self.size = size ** 2
        self.rows = size
        self.cols = size
        self.grid = ['-'] * 9
        self.open_squares = set()
        for i in range(9):
            self.open_squares.add(i)
        self. winning_boards = ((0, 1, 2), (3, 4, 5), (6, 7, 8),
                                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                (0, 4, 8), (2, 4, 6))

    def print(self):
        for r in range(self.rows):
            for c in range(self.cols):
                print(self.at(r * self.cols + c), end='')
            print()

    def set(self, pos, val):
        if pos in self.open_squares:
            self.grid[pos] = val
            self.open_squares -= {pos}
        else:
            fmt = "Cannot set [{}] to {}"
            raise Exception(fmt.format(pos, val))

    def at(self, pos):
        if 0 <= pos < self.size:
            return self.grid[pos]
        else:
            raise Exception("Cannot access cell {}".format(pos))

    def check_win(self):
        for board in self.winning_boards:
            if (self.at(board[0]) in "XO") and \
               (self.at(board[0]) == self.at(board[1])) and \
               (self.at(board[0]) == self.at(board[2])):
                return self.at(board[0])
        return None

    def get_random_valid(self):
        return random.sample(self.open_squares, 1)[0]
