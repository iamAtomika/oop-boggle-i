import string
import random


class BoggleBoard:

    def __init__(self):
        self._letters = string.ascii_uppercase
        self.board = []

    def shake(self):
        shake_it = list(self._letters)
        random.shuffle(shake_it)
        self.board = shake_it
        print(shake_it)


boggle_board = BoggleBoard()
boggle_board.shake()
