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
        self.traits = []

        
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
        proof_color = (63 + (tier * 11), 71 + (tier * 11), 76 + (tier * 11))

        if self.power != None:
            pygame.draw.circle(window, power_color, (x - (tier * s_height), y - (tier * s_height)), h_size * .955)

        if self.selected:
            pygame.draw.circle(window, CYAN, (x - (tier * s_height), y - (tier * s_height)), h_size * .9)
        else:
            pygame.draw.circle(window, BLACK, (x - (tier * s_height), y - (tier * s_height)), h_size * .9)

        if 2 in self.traits:
            pygame.draw.circle(window, proof_color, (x - (tier * s_height), y - (tier * s_height)), h_size * .8)
        else:
            pygame.draw.circle(window, body_color, (x - (tier * s_height), y - (tier * s_height)), h_size * .8)

        if 1 in self.traits:
            image = pygame.transform.scale(pygame.image.load(f'quadradius\Orb\oant.png'), (size * .3, size * .3))
            antenna = pygame.transform.rotate(image, 55)
            z = x - (tier * s_height) - (size * .6)
            t = y - (tier * s_height) - (size // 1.8) 
            window.blit(antenna, (z, t))

        if 3 in self.traits:
            fan = pygame.transform.scale(pygame.image.load(f'quadradius\Orb\ofan.png'), (size * .3, size * .3))
            z = x - (tier * s_height) - (size * .5)
            t = y - (tier * s_height) - (size * .15)
            window.blit(fan, (z, t))
            z = x - (tier * s_height) + (size * .2)
            window.blit(fan, (z, t))

        pygame.draw.circle(window, BLACK, (x - (tier * s_height), y - (tier * s_height)), h_size * .3)
        pygame.draw.circle(window, piece_color, (x - (tier * s_height), y - (tier * s_height)), h_size * .2)
            

    
    def move(self, row, col):
        self.row = row
        self.col = col

    def use(self):
        pass