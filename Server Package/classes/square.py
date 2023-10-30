from .constants import *
import pygame

class Square:

    def __init__(self, row, col, height, selected):
        self.height = height
        self.row = row
        self.col = col
        self.selected = selected # Used in client package
        self.power = None
        self.targeted = False # Used in client package