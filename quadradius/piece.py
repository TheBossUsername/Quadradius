from .constants import *
import pygame
PADDING = 5
RADIUS = SQSZ//2 - PADDING

class Piece:
    def __init__(self, row, col, selected, player):
        self.row = row
        self.col = col
        self.selected = selected
        self.power = None
        self.player = player

        
    def draw(self, width, height, window, tier):
        s_amount = 8
        s_height = height // 100
        size = height // (s_amount + 2)
        h_size = size // 2
        x = (self.col * size) + ((width - (size * s_amount)) // 2) + (size // 2)
        y = (self.row * size) + (height // 10) + (size // 2)
        body_color = (200 + (tier * 11), 200 + (tier * 11), 200 + (tier * 11))
        power_color = (0, 200 + (tier * 11), 0)
        if self.player == 1:
            piece_color = (155 + (tier * 20), 0, 0)
        elif self.player == 2:
            piece_color = (0, 0, 155 + (tier * 20))

        if self.selected:
            if self.power != None:
                pygame.draw.circle(window, power_color, (x - (tier * s_height), y - (tier * s_height)), h_size * .955)
            pygame.draw.circle(window, CYAN, (x - (tier * s_height), y - (tier * s_height)), h_size * .9)
            pygame.draw.circle(window, body_color, (x - (tier * s_height), y - (tier * s_height)), h_size * .8)
            pygame.draw.circle(window, BLACK, (x - (tier * s_height), y - (tier * s_height)), h_size * .3)
            pygame.draw.circle(window, piece_color, (x - (tier * s_height), y - (tier * s_height)), h_size * .2)
        else:
            if self.power != None:
                pygame.draw.circle(window, power_color, (x - (tier * s_height), y - (tier * s_height)), h_size * .955)
            pygame.draw.circle(window, BLACK, (x - (tier * s_height), y - (tier * s_height)), h_size * .9)
            pygame.draw.circle(window, body_color, (x - (tier * s_height), y - (tier * s_height)), h_size * .8)
            pygame.draw.circle(window, BLACK, (x - (tier * s_height), y - (tier * s_height)), h_size * .3)
            pygame.draw.circle(window, piece_color, (x - (tier * s_height), y - (tier * s_height)), h_size * .2)
            

    
    def move(self, row, col):
        self.row = row
        self.col = col

    def use(self):
        pass