#!/usr/bin/python3
#
# Created by Ian Howell on 12/20/17.
# File name: ai.py


class AI:
    def __init__(self, symbol):
        self.symbol = symbol

        # Hack to get the 'other' player symbol
        self.opponent = ({'X', 'O'} - {symbol}).pop()

    def move(self, board):
        pos = board.get_random_valid()
        print(pos)
        return pos
