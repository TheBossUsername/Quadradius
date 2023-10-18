from random import randint
from .constants import *


total = 7
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
        
        if type == 7:
            return ("Grow Quadradius")
        
        
    def use(self, piece, board):
        if self.type == 1:
            for row in range(ROWS):
                for col in range(COLS):
                    square = board.squares[row][col]
                    t1 = piece.traits.count(1)

                    if t1 > 0:
                        if col == piece.col or col == piece.col - t1 or col == piece.col + t1:
                            if square.height >= 5:
                                pass
                            else:
                                square.height += 1

                    elif col == piece.col:
                        if square.height >= 5:
                            pass
                        else:
                            square.height += 1

        if self.type == 2:
            for row in range(ROWS):
                for col in range(COLS):
                    square = board.squares[row][col]
                    t1 = piece.traits.count(1)

                    if t1 > 0:
                        if row == piece.row or col == piece.row - t1 or col == piece.row + t1:
                            if square.height >= 5:
                                pass
                            else:
                                square.height += 1

                    elif row == piece.row:
                        if square.height >= 5:
                            pass
                        else:
                            square.height += 1

        if self.type == 3:
            t1 = piece.traits.count(1)

            if t1 > 0:
                for x in range(t1 - 1 , t1 + 2):
                    for x in range(t1 - 1 , t1 + 2):
                        if (piece.row + y) >= 0 and (piece.row + y) <= 7 and (piece.col + x) >= 0 and (piece.col + x) <= 7:
                            square = board.squares[piece.row + y][piece.col + x]
                            if square.height >= 5:
                                pass
                            else:
                                square.height += 1
            else:
                for x in range(-1 , 2):
                    for y in range(-1 , 2):
                        if (piece.row + y) >= 0 and (piece.row + y) <= 7 and (piece.col + x) >= 0 and (piece.col + x) <= 7:
                            square = board.squares[piece.row + y][piece.col + x]
                            if square.height >= 5:
                                pass
                            else:
                                square.height += 1

        
        if self.type == 4:
            for row in range(ROWS):
                for col in range(COLS):
                    square = board.squares[row][col]
                    t1 = piece.traits.count(1)

                    if t1 > 0:
                        if col == piece.col or col == piece.col - t1 or col == piece.col + t1:
                            if square.height >= 5:
                                pass
                            else:
                                square.height -= 1

                    elif col == piece.col:
                        if square.height >= 5:
                            pass
                        else:
                            square.height -= 1

        if self.type == 5:
            for row in range(ROWS):
                for col in range(COLS):
                    square = board.squares[row][col]
                    t1 = piece.traits.count(1)

                    if t1 > 0:
                        if row == piece.row or col == piece.row - t1 or col == piece.row + t1:
                            if square.height >= 5:
                                pass
                            else:
                                square.height -= 1

                    elif row == piece.row:
                        if square.height >= 5:
                            pass
                        else:
                            square.height -= 1

        if self.type == 6:
            t1 = piece.traits.count(1)

            if t1 > 0:
                for x in range(t1 - 1 , t1 + 2):
                    for x in range(t1 - 1 , t1 + 2):
                        if (piece.row + y) >= 0 and (piece.row + y) <= 7 and (piece.col + x) >= 0 and (piece.col + x) <= 7:
                            square = board.squares[piece.row + y][piece.col + x]
                            if square.height >= 5:
                                pass
                            else:
                                square.height -= 1
            else:
                for x in range(-1 , 2):
                    for y in range(-1 , 2):
                        if (piece.row + y) >= 0 and (piece.row + y) <= 7 and (piece.col + x) >= 0 and (piece.col + x) <= 7:
                            square = board.squares[piece.row + y][piece.col + x]
                            if square.height >= 5:
                                pass
                            else:
                                square.height -= 1

        if self.type == 7:
            piece.traits.append(1)
        