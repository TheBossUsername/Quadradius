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
                if row == 4 and col == 4:
                    self.squares[row].append(Square(row, col, 3, True))
                else:
                    self.squares[row].append(Square(row, col, 3, False))


    def create_pieces(self):
        for row in range(ROWS):
            self.pieces.append([])
            for col in range(COLS):
                if row == 0 or row == 1:
                    self.pieces[row].append(Piece(row, col, False, 2))
                elif row == 6 or row == 7:
                    self.pieces[row].append(Piece(row, col, False, 1))
                else:
                    self.pieces[row].append(None)

    def de_target_squares(self):
        for row in range(ROWS):
            for col in range(COLS):
                square = self.squares[row][col]
                square.targeted = False
                
    def draw(self, window, width, height, timer):
        window.fill(BLACK)
        for tier in range(5):
            for row in range(ROWS):
                for col in range(COLS):
                    square = self.squares[row][col]
                    piece = self.pieces[row][col]
                    square.draw_square(width, height, window, tier, timer)
                    if piece != None  and square.height == tier + 1:
                        piece.draw(width, height, window, tier)
                                                        

    def select_piece(self):
        for row in range(ROWS):
            for col in range(COLS):
                square = self.squares[row][col]
                if square.selected:
                    selected = square
        if self.pieces[selected.row][selected.col] != None:
            selected_piece = self.pieces[selected.row][selected.col]
            selected_piece.selected = True
            return selected_piece
        else:
            return None
    
    def de_select_piece(self):
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.pieces[row][col]
                if piece != None:
                    piece.selected = False
        return None


    def move_piece(self, selected_piece, selected_square):

        new_row = selected_square.row
        new_col = selected_square.col

        if 5 in selected_piece.traits: 
            self.pieces[selected_piece.row][selected_piece.col], self.pieces[new_row][new_col] = Piece(selected_piece.row, selected_piece.col, False, selected_piece.player), self.pieces[selected_piece.row][selected_piece.col]
            selected_piece.traits.remove(5)
            if len(selected_piece.traits) != 0:
                for x in selected_piece.traits:
                    self.pieces[selected_piece.row][selected_piece.col].traits.append(x)
        else:
            self.pieces[selected_piece.row][selected_piece.col], self.pieces[new_row][new_col] = None, self.pieces[selected_piece.row][selected_piece.col]
        selected_piece.move(new_row, new_col)

    def get_selected_square(self):
        for row in range(ROWS):
            for col in range(COLS):
                square = self.squares[row][col]
                if square.selected:
                    return square

    def move_selected_square(self, square, direction):
        old_square = square

        if direction == 1:
            new_row = old_square.row - 1
            new_col = old_square.col
        elif direction == 2:
            new_row = old_square.row 
            new_col = old_square.col + 1
        elif direction == 3:
            new_row = old_square.row + 1
            new_col = old_square.col 
        elif direction == 4:
            new_row = old_square.row 
            new_col = old_square.col - 1
        else:
            print("Error: Could not get new square cordinates")
            return old_square

        if new_row >= 0 and new_col >= 0 and new_row < ROWS and new_col < COLS:
            new_square = self.squares[new_row][new_col]
            old_square.selected = False
            new_square.selected = True
            return new_square         
        else:
            return old_square
        
    def spawn_power(self, row, col, type):
        self.squares[row][col].power = Power()
                