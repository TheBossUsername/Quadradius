from .constants import *
import pygame
import os

class Square:

    def __init__(self, row, col, height, selected):
        self.height = height
        self.row = row
        self.col = col
        self.selected = selected
        self.power = None
        self.targeted = False

    def draw_square(self, width, height, window, tier, timer):
        s_amount = 8
        size = height // (s_amount + 2)
        s_height = height // 100
        x = (self.col * size) + ((width - (size * s_amount)) // 2)
        y = (self.row * size) + (height // 10)

        side_color = (tier * 40, tier * 40, tier * 40)
        top_color = (40 + (tier * 40), 40 + (tier * 40), 40 + (tier * 40))
        red_color = (tier * 63.75, 0, 0)
        targeted_color = (0, 200 + (tier * 11), 0)

        padd = height // 400
        if padd < 2:
            padd = 2

        l_thick = padd
        
        if self.height >= tier + 1:
            if tier > 0:
                if self.height >= tier + 1:
                    if self.height == tier + 1:
                        for z in range(s_height, 0, -1):
                            pygame.draw.rect(window, side_color, (x - (tier * s_height) + z, y - (tier * s_height) + z, size, size))
                        pygame.draw.line(window, BLACK, (x - (tier * s_height) + size, y - (tier * s_height)), (x - ((tier - 1) * s_height) + size, y - ((tier - 1) * s_height)), l_thick)
                        pygame.draw.line(window, BLACK, (x - (tier * s_height), y - (tier * s_height) + size), (x - ((tier - 1) * s_height), y - ((tier - 1) * s_height) + size), l_thick)
                        pygame.draw.line(window, BLACK, (x - (tier * s_height) + size - 1, y - (tier * s_height) + size - 1), (x - ((tier - 1) * s_height) + size, y - ((tier - 1) * s_height) + size), l_thick)
                        pygame.draw.line(window, BLACK, (x - ((tier - 1) * s_height) + size, y - ((tier - 1) * s_height) + size),(x - ((tier - 1) * s_height) + size, y - ((tier - 1) * s_height)), l_thick -1)
                        pygame.draw.line(window, BLACK, (x - ((tier - 1) * s_height) + size, y - ((tier - 1) * s_height) + size),(x - ((tier - 1) * s_height), y - ((tier - 1) * s_height) + size), l_thick -1)
                    else:
                        for z in range(s_height, 0, -1):
                            pygame.draw.rect(window, red_color, (x - (tier * s_height) + z, y - (tier * s_height) + z, size, size))
                        pygame.draw.line(window, BLACK, (x - (tier * s_height) + size, y - (tier * s_height)), (x - ((tier - 1) * s_height) + size, y - ((tier - 1) * s_height)), l_thick)
                        pygame.draw.line(window, BLACK, (x - (tier * s_height), y - (tier * s_height) + size), (x - ((tier - 1) * s_height), y - ((tier - 1) * s_height) + size), l_thick)
                        pygame.draw.line(window, BLACK, (x - (tier * s_height) + size, y - (tier * s_height) + size), (x - ((tier - 1) * s_height) + size, y - ((tier - 1) * s_height) + size), l_thick)
                        pygame.draw.line(window, BLACK, (x - ((tier - 1) * s_height) + size, y - ((tier - 1) * s_height) + size),(x - ((tier - 1) * s_height) + size, y - ((tier - 1) * s_height)), l_thick -1)
                        pygame.draw.line(window, BLACK, (x - ((tier - 1) * s_height) + size, y - ((tier - 1) * s_height) + size),(x - ((tier - 1) * s_height), y - ((tier - 1) * s_height) + size), l_thick -1)
                
                    # Draw top
                    if self.targeted:
                        pygame.draw.rect(window, BLACK, (x - (tier * s_height), y - (tier * s_height), size, size)) 
                        pygame.draw.rect(window, targeted_color, (x - (tier * s_height) + padd, y - (tier * s_height) + padd, size - (padd * 2), size - (padd * 2)))
                        pygame.draw.rect(window, top_color, (x - (tier * s_height) + padd * 2, y - (tier * s_height) + padd * 2, size - (padd * 4), size - (padd * 4)))
                    elif self.selected and self.height == tier + 1:
                        pygame.draw.rect(window, CYAN, (x - (tier * s_height), y - (tier * s_height), size, size)) 
                        pygame.draw.rect(window, top_color, (x - (tier * s_height) + padd * 2, y - (tier * s_height) + padd * 2, size - (padd * 4), size - (padd * 4)))
                    else:
                        pygame.draw.rect(window, BLACK, (x - (tier * s_height), y - (tier * s_height), size, size)) 
                        pygame.draw.rect(window, top_color, (x - (tier * s_height) + padd, y - (tier * s_height) + padd, size - (padd * 2), size - (padd * 2)))
                    # Draw power up circle    
                    if self.power != None and self.height == tier + 1:
                        t = timer % 30
                        image = (f"orb{t}.png")
                        path = os.path.join("classes", "Orb", image)
                        orb = pygame.transform.scale(pygame.image.load(path), (size, size * .60))
                        x = x - (tier * s_height)  
                        y = y - (tier * s_height) + (size * .22) 
                        window.blit(orb, (x, y)) 
                        

            else:
                # Draw top
                if self.targeted:
                    pygame.draw.rect(window, BLACK, (x - (tier * s_height), y - (tier * s_height), size, size)) 
                    pygame.draw.rect(window, targeted_color, (x - (tier * s_height) + padd, y - (tier * s_height) + padd, size - (padd * 2), size - (padd * 2)))
                    pygame.draw.rect(window, top_color, (x - (tier * s_height) + padd * 2, y - (tier * s_height) + padd * 2, size - (padd * 4), size - (padd * 4)))
                elif self.selected and self.height == tier + 1:
                    pygame.draw.rect(window, CYAN, (x - (tier * s_height), y - (tier * s_height), size, size)) 
                    pygame.draw.rect(window, top_color, (x - (tier * s_height) + padd * 2, y - (tier * s_height) + padd * 2, size - (padd * 4), size - (padd * 4)))
                else:
                    pygame.draw.rect(window, BLACK, (x - (tier * s_height), y - (tier * s_height), size, size)) 
                    pygame.draw.rect(window, top_color, (x - (tier * s_height) + padd, y - (tier * s_height) + padd, size - (padd * 2), size - (padd * 2)))
                # Draw power up circle    
                if self.power != None and self.height == tier + 1:
                        t = timer % 30
                        image = (f"orb{t}.png")
                        path = os.path.join("classes", "Orb", image)
                        orb = pygame.transform.scale(pygame.image.load(path), (size, size * .60))
                        x = x - (tier * s_height)  
                        y = y - (tier * s_height) + (size * .22) 
                        window.blit(orb, (x, y))

        

