#!/usr/bin/python3
#
# Created by Ian Howell on 12/20/17.
# File name: ai.py
import random


class AI:
    def __init__(self, symbol):
        self.symbol = symbol

        # Hack to get the 'other' player symbol
        self.opponent = ({'X', 'O'} - {symbol}).pop()

    def move(self, board):
        possible = [x for x in range(9) if board.at(x) not in 'XO']
        best = -2
        best_move = None
        for position in possible:
            board.set(position, self.symbol)
            move_val = self.__get_best_move(board)
            board.unset(position)

            if move_val > best:
                best = move_val
                best_move = position
            elif (move_val == best) and random.choice([True, False]):
                # To make it nondeterministic
                best = move_val
                best_move = position

        print(best_move)
        return best_move

    def __get_best_move(self, board, my_turn=False):
        possible = [x for x in range(9) if board.at(x) not in 'XO']
        score = self.__evaluate(board)

        # Base case
        if (score != 0) or (len(possible) == 0):
            return score

        if my_turn:
            best = -2
            for position in possible:
                board.set(position, self.symbol)
                best = max(best, self.__get_best_move(board, not my_turn))
                board.unset(position)
            return best
        else:
            best = 2
            for position in possible:
                board.set(position, self.opponent)
                best = min(best, self.__get_best_move(board, not my_turn))
                board.unset(position)
            return best

    def __evaluate(self, board):
        winner = board.check_win()
        if winner:
            return 1 if (winner == self.symbol) else -1
        return 0
