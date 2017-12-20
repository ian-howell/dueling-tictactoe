#!/usr/bin/python3
#
# Created by Ian Howell on 12/20/17.
# File name: grid.py


class Grid:
    def __init__(self, size=3):
        self.size = size ** 2
        self.rows = size
        self.cols = size
        self.grid = ['-'] * 9

    def print(self):
        for r in range(self.rows):
            for c in range(self.cols):
                print(self.at(r, c), end='')
            print()

    def set(self, r, c, val):
        if not self.__is_valid(r, c):
            fmt = "Cannot set ({}, {}) to {} (current val = {})"
            raise Exception(fmt.format(r, c, val, self.at(r, c)))
        self.grid[self.__index(r, c)] = val

    def at(self, r, c):
        if (r < 0) or (r >= self.rows) or (c < 0) or (c >= self.cols):
            fmt = "Cannot access row {}, col {}"
            raise Exception(fmt.format(r, c))
        return self.grid[self.__index(r, c)]

    def __index(self, r, c):
        return r * self.cols + c

    def __is_valid(self, r, c):
        return self.at(r, c) == '-'
