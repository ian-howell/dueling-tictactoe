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

        return best_move

    def __get_best_move(self, board, my_turn=False):
        possible = [x for x in range(9) if board.at(x) not in 'XO']
        score = self.__evaluate(board)

        # Base case
        if (score != 0) or (len(possible) == 0):
            return score

        best = -2 if my_turn else 2
        minmax = max if my_turn else min
        symbol = self.symbol if my_turn else self.opponent

        for position in possible:
            board.set(position, symbol)
            best = minmax(best, self.__get_best_move(board, not my_turn))
            board.unset(position)
        return best

    def __evaluate(self, board):
        winner = board.check_win()
        if winner:
            return 1 if (winner == self.symbol) else -1
        return 0

    def random_nonsense(self):
        things = ("Good move!", "Hmm...", "I'm thinking", "You're on!",
                  "Really?", "Rookie mistake...", "I'm gonna win!",
                  "That was dumb!", "My turn!", "WTF?!?", "Here I come ;)")
        return random.sample(things, 1)[0]
