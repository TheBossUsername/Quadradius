from random import randint
from .constants import *


total = 25
class Power:

    def __init__(self):
        self.type = randint(1, total)
    
    def get_name(self):

        if self.type == 1:
            return ("Wall column")
        
        if self.type == 2:
            return ("Wall Row")
        
        if self.type == 3:
            return ("Plateau")
        
        if self.type == 4:
            return ("Trench column")
        
        if self.type == 5:
            return ("Trench Row")
        
        if self.type == 6:
            return ("Moat")
        
        if self.type == 7:
            return ("Grow Quadradius")
        
        if self.type == 8:
            return ("Lower Tile")
        
        if self.type == 9:
            return ("Raise Tile")
        
        if self.type == 10:
            return ("Jump Proof")
        
        if self.type == 11:
            return ("Climb")
        
        if self.type == 12:
            return ("Dredge Column")
        
        if self.type == 13:
            return ("Dredge Row")
        
        if self.type == 14:
            return ("Dredge Radial")
        
        if self.type == 15:
            return ("Move Diagonal")
        
        if self.type == 16:
            return ("Multiply")
        
        if self.type == 17:
            return ("Invert Column")
        
        if self.type == 18:
            return ("Invert Row")
        
        if self.type == 19:
            return ("Invert Radial")
        
        if self.type == 20:
            return ("Kamikaze Column")
        
        if self.type == 21:
            return ("Kamikaze Row")
        
        if self.type == 22:
            return ("Kamikaze Radial")
        
        if self.type == 23:
            return ("Destroy Column")
        
        if self.type == 24:
            return ("Destroy Row")
        
        if self.type == 25:
            return ("Destroy Radial")
        
    def show_targets(self, piece, board):
        # Columns
        if self.type == 1 or self.type == 4 or self.type == 17:
            t1 = piece.traits.count(1)
            if t1 > 0:
                for r in range(-t1, t1 + 1):
                    if piece.col + r >= 0 and piece.col + r <= 7:
                        for x in range(8):
                            square = board.squares[x][piece.col + r]
                            square.targeted = True
            else:
                for x in range(8):
                    square = board.squares[x][piece.col]
                    square.targeted = True
        
        # Rows
        if self.type == 2 or self.type == 5 or self.type == 18:
            t1 = piece.traits.count(1)
            if t1 > 0:
                for r in range(-t1, t1 + 1):
                    if piece.row + r >= 0 and piece.row + r <= 7:
                        for square in board.squares[piece.row + r]:
                            square.targeted = True
            else:
                for square in board.squares[piece.row]:
                    square.targeted = True

        # Radials
        if self.type == 3 or self.type == 6 or self.type == 19:
            t1 = piece.traits.count(1)

            if t1 > 0:
                for x in range(-t1 -1 , t1 + 2):
                    for y in range(-t1 - 1, t1 + 2):
                        if (piece.row + y) >= 0 and (piece.row + y) <= 7 and (piece.col + x) >= 0 and (piece.col + x) <= 7:
                            square = board.squares[piece.row + y][piece.col + x]
                            square.targeted = True
            else:
                for x in range(-1 , 2):
                    for y in range(-1 , 2):
                        if (piece.row + y) >= 0 and (piece.row + y) <= 7 and (piece.col + x) >= 0 and (piece.col + x) <= 7:
                            square = board.squares[piece.row + y][piece.col + x]
                            square.targeted = True

        #Powers
        if self.type == 7 or self.type == 8 or self.type == 9 or self.type == 10 or self.type == 11 or self.type == 15 or self.type == 16:
            board.squares[piece.row][piece.col].targeted = True

        # Friendly Columns
        if False:
            t1 = piece.traits.count(1)
            if t1 > 0:
                for r in range(-t1, t1 + 1):
                    if piece.col + r >= 0 and piece.col + r <= 7:
                        for x in range(8):
                            if board.pieces[x][piece.col + r] != None:
                                if board.pieces[x][piece.col].player == piece.player:
                                    square = board.squares[x][piece.col]
                                    square.targeted = True
            else:
                for x in range(8):
                    if board.pieces[x][piece.col] != None:
                        if board.pieces[x][piece.col].player == piece.player:
                            square = board.squares[x][piece.col]
                            square.targeted = True
        
        # Friendly Rows
        if False:
            t1 = piece.traits.count(1)
            if t1 > 0:
                for r in range(-t1, t1 + 1):
                    if piece.row + r >= 0 and piece.row + r <= 7:
                        for square in board.squares[piece.row + r]:
                            if board.pieces[square.row][square.col] != None:
                                if board.pieces[square.row][square.col].player == piece.player:
                                    square.targeted = True
            else:
                for square in board.squares[piece.row]:
                    if board.pieces[square.row][square.col] != None:
                        if board.pieces[square.row][square.col].player == piece.player:
                            square.targeted = True

        # Friendly Radials
        if False:
            t1 = piece.traits.count(1)

            if t1 > 0:
                for x in range(-t1 -1 , t1 + 2):
                    for y in range(-t1 - 1, t1 + 2):
                        if (piece.row + y) >= 0 and (piece.row + y) <= 7 and (piece.col + x) >= 0 and (piece.col + x) <= 7:
                            if board.pieces[piece.row + y][piece.col + x] != None:
                                if board.pieces[piece.row + y][piece.col + x].player == piece.player:
                                    square = board.squares[piece.row + y][piece.col + x]
                                    square.targeted = True
            else:
                for x in range(-1 , 2):
                    for y in range(-1 , 2):
                        if (piece.row + y) >= 0 and (piece.row + y) <= 7 and (piece.col + x) >= 0 and (piece.col + x) <= 7:
                            if board.pieces[piece.row + y][piece.col + x] != None:
                                if board.pieces[piece.row + y][piece.col + x].player == piece.player:
                                    square = board.squares[piece.row + y][piece.col + x]
                                    square.targeted = True

        # Enemy Columns
        if self.type == 23:
            t1 = piece.traits.count(1)
            if t1 > 0:
                for r in range(-t1, t1 + 1):
                    if piece.col + r >= 0 and piece.col + r <= 7:
                        for x in range(8):
                            if board.pieces[x][piece.col + r] != None:
                                if board.pieces[x][piece.col].player != piece.player:
                                    square = board.squares[x][piece.col]
                                    square.targeted = True
            else:
                for x in range(8):
                    if board.pieces[x][piece.col] != None:
                        if board.pieces[x][piece.col].player != piece.player:
                            square = board.squares[x][piece.col]
                            square.targeted = True
        
        # Enemy Rows
        if self.type == 24:
            t1 = piece.traits.count(1)
            if t1 > 0:
                for r in range(-t1, t1 + 1):
                    if piece.row + r >= 0 and piece.row + r <= 7:
                        for square in board.squares[piece.row + r]:
                            if board.pieces[square.row][square.col] != None:
                                if board.pieces[square.row][square.col].player != piece.player:
                                    square.targeted = True
            else:
                for square in board.squares[piece.row]:
                    if board.pieces[square.row][square.col] != None:
                        if board.pieces[square.row][square.col].player != piece.player:
                            square.targeted = True

        # Enemy Radials
        if self.type == 25:
            t1 = piece.traits.count(1)

            if t1 > 0:
                for x in range(-t1 -1 , t1 + 2):
                    for y in range(-t1 - 1, t1 + 2):
                        if (piece.row + y) >= 0 and (piece.row + y) <= 7 and (piece.col + x) >= 0 and (piece.col + x) <= 7:
                            if board.pieces[piece.row + y][piece.col + x] != None:
                                if board.pieces[piece.row + y][piece.col + x].player != piece.player:
                                    square = board.squares[piece.row + y][piece.col + x]
                                    square.targeted = True
            else:
                for x in range(-1 , 2):
                    for y in range(-1 , 2):
                        if (piece.row + y) >= 0 and (piece.row + y) <= 7 and (piece.col + x) >= 0 and (piece.col + x) <= 7:
                            if board.pieces[piece.row + y][piece.col + x] != None:
                                if board.pieces[piece.row + y][piece.col + x].player != piece.player:
                                    square = board.squares[piece.row + y][piece.col + x]
                                    square.targeted = True
        # All Columns
        if self.type == 12 or self.type == 20:
            t1 = piece.traits.count(1)
            if t1 > 0:
                for r in range(-t1, t1 + 1):
                    if piece.col + r >= 0 and piece.col + r <= 7:
                        for x in range(8):
                            if board.pieces[x][piece.col + r] != None:
                                square = board.squares[x][piece.col + r]
                                square.targeted = True
            else:
                for x in range(8):
                    if board.pieces[x][piece.col] != None:
                        square = board.squares[x][piece.col]
                        square.targeted = True
        
        # All Rows
        if self.type == 13 or self.type == 21:
            t1 = piece.traits.count(1)
            if t1 > 0:
                for r in range(-t1, t1 + 1):
                    if piece.row + r >= 0 and piece.row + r <= 7:
                        for square in board.squares[piece.row + r]:
                            if board.pieces[square.row][square.col] != None:
                                square.targeted = True
            else:
                for square in board.squares[piece.row]:
                    if board.pieces[square.row][square.col] != None:
                        square.targeted = True

        # All Radials
        if self.type == 14 or self.type == 22:
            t1 = piece.traits.count(1)

            if t1 > 0:
                for x in range(-t1 -1 , t1 + 2):
                    for y in range(-t1 - 1, t1 + 2):
                        if (piece.row + y) >= 0 and (piece.row + y) <= 7 and (piece.col + x) >= 0 and (piece.col + x) <= 7:
                            square = board.squares[piece.row + y][piece.col + x]
                            square.targeted = True
            else:
                for x in range(-1 , 2):
                    for y in range(-1 , 2):
                        if (piece.row + y) >= 0 and (piece.row + y) <= 7 and (piece.col + x) >= 0 and (piece.col + x) <= 7:
                            if board.pieces[piece.row + y][piece.col + x] != None:
                                square = board.squares[piece.row + y][piece.col + x]
                                square.targeted = True

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

        # Multiply
        if self.type == 16:
            if 5 not in piece.traits:
                piece.traits.append(5)

        # Invert Column
        if self.type == 17:
            t1 = piece.traits.count(1)
            if t1 > 0:
                for r in range(-t1, t1 + 1):
                    if piece.col + r >= 0 and piece.col + r <= 7:
                        for x in range(8):
                            square = board.squares[x][piece.col + r]
                            if square.height == 3:
                                pass
                            elif square.height == 2:
                                square.height = 4
                            elif square.height == 1:
                                square.height = 5
                            elif square.height == 4:
                                square.height = 2
                            elif square.height == 5:
                                square.height = 1
            else:
                for x in range(8):
                    square = board.squares[x][piece.col]
                    if square.height == 3:
                        pass
                    elif square.height == 2:
                        square.height = 4
                    elif square.height == 1:
                        square.height = 5
                    elif square.height == 4:
                        square.height = 2
                    elif square.height == 5:
                        square.height = 1

        # Invert Row
        if self.type == 18:
            t1 = piece.traits.count(1)
            if t1 > 0:
                for r in range(-t1, t1 + 1):
                    if piece.row + r >= 0 and piece.row + r <= 7:
                        for square in board.squares[piece.row + r]:
                            if square.height == 3:
                                pass
                            elif square.height == 2:
                                square.height = 4
                            elif square.height == 1:
                                square.height = 5
                            elif square.height == 4:
                                square.height = 2
                            elif square.height == 5:
                                square.height = 1
            else:
                for square in board.squares[piece.row]:
                    if square.height == 3:
                        pass
                    elif square.height == 2:
                        square.height = 4
                    elif square.height == 1:
                        square.height = 5
                    elif square.height == 4:
                        square.height = 2
                    elif square.height == 5:
                        square.height = 1

        # Invert Radial
        if self.type == 19:
            t1 = piece.traits.count(1)

            if t1 > 0:
                for x in range(-t1 -1 , t1 + 2):
                    for y in range(-t1 - 1, t1 + 2):
                        if (piece.row + y) >= 0 and (piece.row + y) <= 7 and (piece.col + x) >= 0 and (piece.col + x) <= 7:
                            square = board.squares[piece.row + y][piece.col + x]
                            if square.height == 3:
                                pass
                            elif square.height == 2:
                                square.height = 4
                            elif square.height == 1:
                                square.height = 5
                            elif square.height == 4:
                                square.height = 2
                            elif square.height == 5:
                                square.height = 1
            else:
                for x in range(-1 , 2):
                    for y in range(-1 , 2):
                        if (piece.row + y) >= 0 and (piece.row + y) <= 7 and (piece.col + x) >= 0 and (piece.col + x) <= 7:
                            square = board.squares[piece.row + y][piece.col + x]
                            if square.height == 3:
                                pass
                            elif square.height == 2:
                                square.height = 4
                            elif square.height == 1:
                                square.height = 5
                            elif square.height == 4:
                                square.height = 2
                            elif square.height == 5:
                                square.height = 1

        
        # Kamikaze Column
        if self.type == 20:
            t1 = piece.traits.count(1)
            if t1 > 0:
                for r in range(-t1, t1 + 1):
                    if piece.col + r >= 0 and piece.col + r <= 7:
                        for x in range(8):
                            square = board.squares[x][piece.col + r]
                            tp = board.pieces[square.row][square.col]
                            if tp != None:
                                board.pieces[square.row][square.col] = None
            else:
                for x in range(8):
                    square = board.squares[x][piece.col]
                    tp = board.pieces[square.row][square.col]
                    if tp != None:
                        board.pieces[square.row][square.col] = None
        
        # Kamikaze Row
        if self.type == 21:
            t1 = piece.traits.count(1)
            if t1 > 0:
                for r in range(-t1, t1 + 1):
                    if piece.row + r >= 0 and piece.row + r <= 7:
                        for square in board.squares[piece.row + r]:
                            tp = board.pieces[square.row][square.col]
                            if tp != None:
                                board.pieces[square.row][square.col] = None
            else:
                for square in board.squares[piece.row]:
                    tp = board.pieces[square.row][square.col]
                    if tp != None:
                        board.pieces[square.row][square.col] = None
                    

        # Kamikaze Radial
        if self.type == 22:
            t1 = piece.traits.count(1)

            if t1 > 0:
                for x in range(-t1 -1 , t1 + 2):
                    for y in range(-t1 - 1, t1 + 2):
                        if (piece.row + y) >= 0 and (piece.row + y) <= 7 and (piece.col + x) >= 0 and (piece.col + x) <= 7:
                            square = board.squares[piece.row + y][piece.col + x]
                            tp = board.pieces[square.row][square.col]
                            if tp != None:
                                board.pieces[square.row][square.col] = None
                                    

            else:
                for x in range(-1 , 2):
                    for y in range(-1 , 2):
                        if (piece.row + y) >= 0 and (piece.row + y) <= 7 and (piece.col + x) >= 0 and (piece.col + x) <= 7:
                            square = board.squares[piece.row + y][piece.col + x]
                            tp = board.pieces[square.row][square.col]
                            if tp != None:
                                board.pieces[square.row][square.col] = None

        # Destroy Column
        if self.type == 23:
            t1 = piece.traits.count(1)
            if t1 > 0:
                for r in range(-t1, t1 + 1):
                    if piece.col + r >= 0 and piece.col + r <= 7:
                        for x in range(8):
                            square = board.squares[x][piece.col + r]
                            tp = board.pieces[square.row][square.col]
                            if tp != None:
                                if tp.player != piece.player:
                                    board.pieces[square.row][square.col] = None
            else:
                for x in range(8):
                    square = board.squares[x][piece.col]
                    tp = board.pieces[square.row][square.col]
                    if tp != None:
                        if tp.player != piece.player:
                            board.pieces[square.row][square.col] = None
        
        # Destroy Row
        if self.type == 24:
            t1 = piece.traits.count(1)
            if t1 > 0:
                for r in range(-t1, t1 + 1):
                    if piece.row + r >= 0 and piece.row + r <= 7:
                        for square in board.squares[piece.row + r]:
                            tp = board.pieces[square.row][square.col]
                            if tp != None:
                                if tp.player != piece.player:
                                    board.pieces[square.row][square.col] = None
            else:
                for square in board.squares[piece.row]:
                    tp = board.pieces[square.row][square.col]
                    if tp != None:
                        if tp.player != piece.player:
                            board.pieces[square.row][square.col] = None
                    

        # Destroy Radial
        if self.type == 25:
            t1 = piece.traits.count(1)

            if t1 > 0:
                for x in range(-t1 -1 , t1 + 2):
                    for y in range(-t1 - 1, t1 + 2):
                        if (piece.row + y) >= 0 and (piece.row + y) <= 7 and (piece.col + x) >= 0 and (piece.col + x) <= 7:
                            square = board.squares[piece.row + y][piece.col + x]
                            tp = board.pieces[square.row][square.col]
                            if tp != None:
                                if tp.player != piece.player:
                                    board.pieces[square.row][square.col] = None
                                    

            else:
                for x in range(-1 , 2):
                    for y in range(-1 , 2):
                        if (piece.row + y) >= 0 and (piece.row + y) <= 7 and (piece.col + x) >= 0 and (piece.col + x) <= 7:
                            square = board.squares[piece.row + y][piece.col + x]
                            tp = board.pieces[square.row][square.col]
                            if tp != None:
                                if tp.player != piece.player:
                                    board.pieces[square.row][square.col] = None
                            