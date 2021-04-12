from tictactoe import TicTacToe
from random import choice


class RandomPlayer:

    def __init__(self, game, mark):
        self.mark = mark
        self.game = game

    def make_move(self):
        empty_squares = self.game.get_empty_squares()

        try:
            choice(empty_squares).mark = self.mark
        except IndexError:
            pass
