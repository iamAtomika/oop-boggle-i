import string
import random


class BoggleBoard:

    def __init__(self):
        # self._letters = string.ascii_uppercase #none of the letters repeat tho
        self.board = []
        self.letter_dice = [
            "AAEEGN", "ELRTTY", "AOOTTW", "ABBJOO",
            "EHRTVW", "CIMOTU", "DISTTY", "EIOSST",
            "DELRVY", "ACHOPS", "HIMNQU", "EEINSU",
            "EEGHNW", "AFFKPS", "HLNNRZ", "DEILRX"
        ]
        ##combos requested by readme

    def shake(self):
        # shake_it = list(self._letters)
        # random.shuffle(shake_it)
        # self.board = shake_it
        # print(shake_it) #returns all of them in one row

        shake_it = []
        for i in self.letter_dice:
            random_letter = random.choice(i)
            shake_it.append(random_letter)

        self.board = []
        for i in range(0,16,4): #16/4=4
            boggle_row = shake_it[i : i + 4]  
            self.board.append(boggle_row)

        for row in self.board:
            print(' '.join(row))


boggle_board = BoggleBoard()
boggle_board.shake()
