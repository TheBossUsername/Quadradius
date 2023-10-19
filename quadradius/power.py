from random import randint
from .constants import *


total = 15
class Power:

    def __init__(self):
        self.type = randint(1, total)
        self.description = self.get_description(self.type)
    
    def get_description(self, type):

        if type == 1:
            return ("Wall column")
        
        if type == 2:
            return ("Wall Row")
        
        if type == 3:
            return ("Plateau")
        
        if type == 4:
            return ("Trench column")
        
        if type == 5:
            return ("Trench Row")
        
        if type == 6:
            return ("Moat")
        
        if type == 7:
            return ("Grow Quadradius")
        
        if type == 8:
            return ("Lower Tile")
        
        if type == 9:
            return ("Raise Tile")
        
        if type == 10:
            return ("Jump Proof")
        
        if type == 11:
            return ("Climb")
        
        if type == 12:
            return ("Dredge Column")
        
        if type == 13:
            return ("Dredge Row")
        
        if type == 14:
            return ("Dredge Radial")
        
        if type == 15:
            return ("Move Diagonal")
        
    def use(self, piece, board):
        # Wall column
        if self.type == 1:
            t1 = piece.traits.count(1)
            if t1 > 0:
                for r in range(-t1, t1 + 1):
                    if piece.col + r >= 0 and piece.col + r <= 7:
                        for x in range(8):
                            square = board.squares[x][piece.col + r]
                            square.height = 5
            else:
                for x in range(8):
                    square = board.squares[x][piece.col]
                    square.height = 5
        # Wall Row
        if self.type == 2:
            t1 = piece.traits.count(1)
            if t1 > 0:
                for r in range(-t1, t1 + 1):
                    if piece.row + r >= 0 and piece.row + r <= 7:
                        for square in board.squares[piece.row + r]:
                            square.height = 5
            else:
                for square in board.squares[piece.row]:
                    square.height = 5
        # Plateau
        if self.type == 3:
            t1 = piece.traits.count(1)

            if t1 > 0:
                for x in range(-t1 -1 , t1 + 2):
                    for y in range(-t1 - 1, t1 + 2):
                        if (piece.row + y) >= 0 and (piece.row + y) <= 7 and (piece.col + x) >= 0 and (piece.col + x) <= 7:
                            square = board.squares[piece.row + y][piece.col + x]
                            square.height = 5
            else:
                for x in range(-1 , 2):
                    for y in range(-1 , 2):
                        if (piece.row + y) >= 0 and (piece.row + y) <= 7 and (piece.col + x) >= 0 and (piece.col + x) <= 7:
                            square = board.squares[piece.row + y][piece.col + x]
                            square.height = 5
        # Trench column
        if self.type == 4:
            t1 = piece.traits.count(1)
            if t1 > 0:
                for r in range(-t1, t1 + 1):
                    if piece.col + r >= 0 and piece.col + r <= 7:
                       for x in range(8):
                            square = board.squares[x][piece.col + r]
                            square.height = 1
            else:
                for x in range(8):
                    square = board.squares[x][piece.col]
                    square.height = 1
        # Trench Row
        if self.type == 5:
            t1 = piece.traits.count(1)
            if t1 > 0:
                for r in range(-t1, t1 + 1):
                    if piece.row + r >= 0 and piece.row + r <= 7:
                        for square in board.squares[piece.row + r]:
                            square.height = 1
            else:
                for square in board.squares[piece.row]:
                    square.height = 1
        # Moat
        if self.type == 6:
            t1 = piece.traits.count(1)

            if t1 > 0:
                for x in range(-t1 -1 , t1 + 2):
                    for y in range(-t1 - 1, t1 + 2):
                        if (piece.row + y) >= 0 and (piece.row + y) <= 7 and (piece.col + x) >= 0 and (piece.col + x) <= 7:
                            if y == 0 and x == 0:
                                square = board.squares[piece.row][piece.col]
                                square.height = 5
                            else:
                                square = board.squares[piece.row + y][piece.col + x]
                                square.height = 1
            else:
                for x in range(-1 , 2):
                    for y in range(-1 , 2):
                        if (piece.row + y) >= 0 and (piece.row + y) <= 7 and (piece.col + x) >= 0 and (piece.col + x) <= 7:
                            if y == 0 and x == 0:
                                square = board.squares[piece.row][piece.col]
                                square.height = 5
                            else:
                                square = board.squares[piece.row + y][piece.col + x]
                                square.height = 1
        # Grow Quadradius
        if self.type == 7:
            piece.traits.append(1)

        # Lower Tile
        if self.type == 8:
            square = board.squares[piece.row][piece.col]
            if square.height <= 1:
                pass
            else:
                square.height -= 1

        # Raise Tile
        if self.type == 9:
            square = board.squares[piece.row][piece.col]
            if square.height >= 5:
                pass
            else:
                square.height += 1

        # Jump Proof
        if self.type == 10:
            if 2 not in piece.traits:
                piece.traits.append(2)

        # Climb
        if self.type == 11:
            if 3 not in piece.traits:
                piece.traits.append(3)

        # Dredge Column
        if self.type == 12:
            t1 = piece.traits.count(1)
            if t1 > 0:
                for r in range(-t1, t1 + 1):
                    if piece.col + r >= 0 and piece.col + r <= 7:
                        for x in range(8):
                            square = board.squares[x][piece.col + r]
                            tp = board.pieces[square.row][square.col]
                            if tp != None:
                                if tp.player == piece.player:
                                    square.height = 5
                                else:
                                    square.height = 1
            else:
                for x in range(8):
                    square = board.squares[x][piece.col]
                    tp = board.pieces[square.row][square.col]
                    if tp != None:
                        if tp.player == piece.player:
                            square.height = 5
                        else:
                            square.height = 1

        # Dredge Row
        if self.type == 13:
            t1 = piece.traits.count(1)
            if t1 > 0:
                for r in range(-t1, t1 + 1):
                    if piece.row + r >= 0 and piece.row + r <= 7:
                        for square in board.squares[piece.row + r]:
                            tp = board.pieces[square.row][square.col]
                            if tp != None:
                                if tp.player == piece.player:
                                    square.height = 5
                                else:
                                    square.height = 1
            else:
                for square in board.squares[piece.row]:
                    tp = board.pieces[square.row][square.col]
                    if tp != None:
                        if tp.player == piece.player:
                            square.height = 5
                        else:
                            square.height = 1

        # Dredge Radial
        if self.type == 14:
            t1 = piece.traits.count(1)

            if t1 > 0:
                for x in range(-t1 -1 , t1 + 2):
                    for y in range(-t1 - 1, t1 + 2):
                        if (piece.row + y) >= 0 and (piece.row + y) <= 7 and (piece.col + x) >= 0 and (piece.col + x) <= 7:
                            square = board.squares[piece.row + y][piece.col + x]
                            tp = board.pieces[square.row][square.col]
                            if tp != None:
                                if tp.player == piece.player:
                                    square.height = 5
                                else:
                                    square.height = 1

            else:
                for x in range(-1 , 2):
                    for y in range(-1 , 2):
                        if (piece.row + y) >= 0 and (piece.row + y) <= 7 and (piece.col + x) >= 0 and (piece.col + x) <= 7:
                            square = board.squares[piece.row + y][piece.col + x]
                            tp = board.pieces[square.row][square.col]
                            if tp != None:
                                if tp.player == piece.player:
                                    square.height = 5
                                else:
                                    square.height = 1

        # Move Diagonal
        if self.type == 15:
            if 4 not in piece.traits:
                piece.traits.append(4)