from random import randint
from .constants import *


total = 6
class Power:

    def __init__(self):
        self.type = randint(1, total)
        self.description = self.get_description(self.type)
    
    def get_description(self, type):

        if type == 1:
            return ("Raise column")
        
        if type == 2:
            return ("Raise Row")
        
        if type == 3:
            return ("Raise Radial")
        
        if type == 4:
            return ("Lower column")
        
        if type == 5:
            return ("Lower Row")
        
        if type == 6:
            return ("Lower Radial")
        
        
    def use(self, target_row, target_col, board):
        if self.type == 1:
            for row in range(ROWS):
                for col in range(COLS):
                    if col == target_col:
                        square = board.squares[row][col]
                        if square.height >= 5:
                            pass
                        else:
                            square.height += 1

        if self.type == 2:
            for row in range(ROWS):
                for col in range(COLS):
                    if row == target_row:
                        square = board.squares[row][col]
                        if square.height >= 5:
                            pass
                        else:
                            square.height += 1

        if self.type == 3:
            for x in range(-1 , 2):
                for y in range(-1 , 2):
                    if (target_row + y) >= 0 and (target_row + y) <= 7 and (target_col + x) >= 0 and (target_col + x) <= 7:
                        square = board.squares[target_row + y][target_col + x]
                        if square.height >= 5:
                            pass
                        else:
                            square.height += 1

        
        if self.type == 4:
            for row in range(ROWS):
                for col in range(COLS):
                    if col == target_col:
                        square = board.squares[row][col]
                        if square.height <= 1:
                            pass
                        else:
                            square.height -= 1

        if self.type == 5:
            for row in range(ROWS):
                for col in range(COLS):
                    if row == target_row:
                        square = board.squares[row][col]
                        if square.height <= 1:
                            pass
                        else:
                            square.height -= 1

        if self.type == 6:
            for x in range(-1 , 2):
                for y in range(-1 , 2):
                    if (target_row + y) >= 0 and (target_row + y) <= 7 and (target_col + x) >= 0 and (target_col + x) <= 7:
                        square = board.squares[target_row + y][target_col + x]
                        if square.height <= 1:
                            pass
                        else:
                            square.height -= 1
        