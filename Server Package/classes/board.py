import pygame
from .constants import *
from .piece import Piece
from .square import Square
from random import randint, choice
from .power import Power

class Board:
    def __init__(self):
        self.pieces = []
        self.squares = []
        self.create_squares()
        self.create_pieces()

    def create_squares(self):
        for row in range(ROWS):
            self.squares.append([])
            for col in range(COLS):
                self.squares[row].append(Square(row, col, 3, False))


    def create_pieces(self): 
        for row in range(ROWS):
            self.pieces.append([])
            for col in range(COLS):
                if row == 0 or row == 1: # Blue pieces in the top 2 rows
                    self.pieces[row].append(Piece(row, col, False, 2))
                elif row == 6 or row == 7: # Red pieces in the bottom 2 rows
                    self.pieces[row].append(Piece(row, col, False, 1))
                else:
                    self.pieces[row].append(None)


    def move_piece(self, selected_piece, selected_square):

        new_row = selected_square.row
        new_col = selected_square.col

        if 5 in selected_piece.traits: # If piece activated multiply, make a copy of it in the square it is leaving
            self.pieces[selected_piece.row][selected_piece.col], self.pieces[new_row][new_col] = Piece(selected_piece.row, selected_piece.col, False, selected_piece.player), self.pieces[selected_piece.row][selected_piece.col]
            selected_piece.traits.remove(5)
            if len(selected_piece.traits) != 0:
                for x in selected_piece.traits:
                    self.pieces[selected_piece.row][selected_piece.col].traits.append(x)
        else: # Move the piece and destroy what was there
            self.pieces[selected_piece.row][selected_piece.col], self.pieces[new_row][new_col] = None, self.pieces[selected_piece.row][selected_piece.col]
        selected_piece.move(new_row, new_col)
        
    def spawn_power(self):
        potential = [] # List of un occupied squares
        for row in range(ROWS):
            for col in range(COLS):
                square = self.squares[row][col]
                piece = self.pieces[row][col]
                if piece == None and square.power == None:
                    potential.append(square)
        if len(potential) != 0:
            chosen = choice(potential) # Choose a random square
            chosen.power = Power() # Give the square a power
            return chosen.row, chosen.col, chosen.power.type # Return info to update player's boards
                