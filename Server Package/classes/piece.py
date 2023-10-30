from .constants import *
import pygame
PADDING = 5
RADIUS = SQSZ//2 - PADDING

class Piece:
    def __init__(self, row, col, selected, player):
        self.row = row
        self.col = col
        self.selected = selected # Used in the client package
        self.powers = []
        self.player = player # Int of which player it belongs to
        self.traits = []

    def use_power(self, board, index):
        self.powers[index].use(self, board)
            
    
    def move(self, row, col):
        self.row = row
        self.col = col