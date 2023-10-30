from random import randint, choice
from .constants import *


total = 28
class Power:

    def __init__(self):
        self.type = randint(1, total)

    def use(self, piece, board): # Changes the board or piece depending on the power type
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

        # Pillage Column
        if self.type == 26:
            t1 = piece.traits.count(1)
            if t1 > 0:
                for r in range(-t1, t1 + 1):
                    if piece.col + r >= 0 and piece.col + r <= 7:
                        for x in range(8):
                            square = board.squares[x][piece.col + r]
                            tp = board.pieces[square.row][square.col]
                            if tp != None:
                                if tp.player != piece.player:
                                    for x in range(len(tp.powers)):
                                        if len(board.pieces[piece.row][piece.col].powers) >= 3:
                                            del piece.powers[0]
                                        board.pieces[piece.row][piece.col].powers.append(tp.powers[x])
                                    tp.powers = []
            else:
                for x in range(8):
                    square = board.squares[x][piece.col]
                    tp = board.pieces[square.row][square.col]
                    if tp != None:
                        if tp.player != piece.player:
                            for x in range(len(tp.powers)):
                                if len(board.pieces[piece.row][piece.col].powers) >= 3:
                                    del piece.powers[0]
                                board.pieces[piece.row][piece.col].powers.append(tp.powers[x])
                            tp.powers = []

        # Pillage Row
        if self.type == 27:
            t1 = piece.traits.count(1)
            if t1 > 0:
                for r in range(-t1, t1 + 1):
                    if piece.row + r >= 0 and piece.row + r <= 7:
                        for square in board.squares[piece.row + r]:
                            tp = board.pieces[square.row][square.col]
                            if tp != None:
                                if tp.player != piece.player:
                                    for x in range(len(tp.powers)):
                                        if len(board.pieces[piece.row][piece.col].powers) >= 3:
                                            del piece.powers[0]
                                        board.pieces[piece.row][piece.col].powers.append(tp.powers[x])
                                    tp.powers = []
            else:
                for square in board.squares[piece.row]:
                    tp = board.pieces[square.row][square.col]
                    if tp != None:
                        if tp.player != piece.player:
                            for x in range(len(tp.powers)):
                                if len(board.pieces[piece.row][piece.col].powers) >= 3:
                                    del piece.powers[0]
                                board.pieces[piece.row][piece.col].powers.append(tp.powers[x])
                            tp.powers = []
                    

        # Destroy Radial
        if self.type == 28:
            t1 = piece.traits.count(1)

            if t1 > 0:
                for x in range(-t1 -1 , t1 + 2):
                    for y in range(-t1 - 1, t1 + 2):
                        if (piece.row + y) >= 0 and (piece.row + y) <= 7 and (piece.col + x) >= 0 and (piece.col + x) <= 7:
                            square = board.squares[piece.row + y][piece.col + x]
                            tp = board.pieces[square.row][square.col]
                            if tp != None:
                                if tp.player != piece.player:
                                    for x in range(len(tp.powers)):
                                        if len(board.pieces[piece.row][piece.col].powers) >= 3:
                                            del piece.powers[0]
                                        board.pieces[piece.row][piece.col].powers.append(tp.powers[x])
                                    tp.powers = []
                                    

            else:
                for x in range(-1 , 2):
                    for y in range(-1 , 2):
                        if (piece.row + y) >= 0 and (piece.row + y) <= 7 and (piece.col + x) >= 0 and (piece.col + x) <= 7:
                            square = board.squares[piece.row + y][piece.col + x]
                            tp = board.pieces[square.row][square.col]
                            if tp != None:
                                if tp.player != piece.player:
                                    for x in range(len(tp.powers)):
                                        if len(board.pieces[piece.row][piece.col].powers) >= 3:
                                            del piece.powers[0]
                                        board.pieces[piece.row][piece.col].powers.append(tp.powers[x])
                                    tp.powers = []
            
        # Relocate
        if self.type == 29:
            potential = []
            for row in range(ROWS):
                for col in range(COLS):
                    square = board.squares[row][col]
                    tp = board.pieces[row][col]
                    if tp == None:
                        potential.append(square)
            if len(potential) != 0:
                chosen = choice(potential)
                board.pieces[piece.row][piece.col], board.pieces[chosen.row][chosen.col] = None, board.pieces[piece.row][piece.col]
                piece.move(chosen.row, chosen.col)
                            