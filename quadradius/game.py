import pygame
from .constants import *
from .piece import Piece
from .square import Square
from .board import Board
from random import randint
from time import sleep
from .power import Power

class Game:

    def __init__(self):
        self.width = 800
        self.height = 800
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.window = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption('Quadradius')
        pygame.init()
        pygame.time.set_timer(pygame.USEREVENT, 100)


    def legal_move(self, selected_piece, selected_square, board):
        tq = selected_square
        sp = selected_piece
        sq = board.squares[sp.row][sp.col]
        if (tq.height - sq.height) >= 2:
            return False
        
        if board.pieces[tq.row][tq.col] != None:
            tp = board.pieces[tq.row][tq.col]
            if tp.player == sp.player:
                return False
            
        if (tq.row, tq.col) == (sp.row + 1, sp.col):
            return True
        elif (tq.row, tq.col) == (sp.row - 1, sp.col):
            return True
        elif (tq.row, tq.col) == (sp.row, sp.col + 1):
            return True
        elif (tq.row, tq.col) == (sp.row, sp.col - 1):
            return True
        else:
            return False

    def check_win(self, board):
        pieces_1 = 0
        pieces_2 = 0
        for row in range(ROWS):
            for col in range(COLS):
                piece = board.pieces[row][col]
                if piece != None:
                    if piece.player == 1:
                        pieces_1 += 1
                    elif piece.player == 2:
                        pieces_2 += 1
        if pieces_1 == 0:
            return 2
        elif pieces_2 == 0:
            return 1
        else:
            return 0
        
    def give_power(self, board):
        for row in range(ROWS):
            for col in range(COLS):
                square = board.squares[row][col]
                piece = board.pieces[row][col]
                if square.power != None and piece != None:
                    piece.power = square.power
                    square.power = None
                


    def run_game(self):
        board = Board()

        turn_end = True
        spawn = 5
        use_power = False
        selected_piece = None
        selected_square = board.get_selected_square()
        turn = randint(1,2)
        timer = 0
        

        running = True
        while running:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.VIDEORESIZE:
                    self.width  = event.w
                    self.height  = event.h
                    self.window = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

                if event.type == pygame.USEREVENT:
                    timer += 1
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if use_power:
                            text = (f"Use: {selected_piece.power.description}? Confirm: Z Back: X")
                        else:
                            selected_square = board.move_selected_square(selected_square, 1)

                    if event.key == pygame.K_RIGHT:
                        if use_power:
                            text = (f"Use: {selected_piece.power.description}? Confirm: Z Back: X")
                        else:
                            selected_square = board.move_selected_square(selected_square, 2)

                    if event.key == pygame.K_DOWN:
                        if use_power:
                            text = (f"Use: {selected_piece.power.description}? Confirm: Z Back: X")
                        else:
                            selected_square = board.move_selected_square(selected_square, 3)

                    if event.key == pygame.K_LEFT:
                        if use_power:
                            text = (f"Use: {selected_piece.power.description}? Confirm: Z Back: X")
                        else:
                            selected_square = board.move_selected_square(selected_square, 4)

                    if event.key == pygame.K_SPACE:
                        if use_power:
                            text = (f"Use: {selected_piece.power.description}? Confirm: Z Back: X")
                        else:
                            if selected_piece == None:
                                selected_piece = board.select_piece()
                                if selected_piece == None:
                                    text = ("No piece was selected")
                                    selected_piece = board.de_select_piece()
                                elif selected_piece.player == turn:
                                    if selected_piece.power != None:
                                        text = (f"Move: Space bar, {selected_piece.power.description}: Z, Back: X")
                                    else:
                                        text = ("Move: Space bar, Back: X")
                                elif selected_piece.player != turn:
                                    text = ("This piece is not yours!")
                                    selected_piece = board.de_select_piece()
                                else:
                                    text = ("Error: Unknown thing selected")
                                    selected_piece = board.de_select_piece()
                            elif selected_piece != None:
                                if self.legal_move(selected_piece, selected_square, board):
                                    board.move_piece()
                                    selected_piece = board.de_select_piece()
                                    turn_end = True
                                else:
                                    text = ("That is not a legal move, Back: X")
                            else:
                                text = ("ERROR with piece")

                    if event.key == pygame.K_x:
                        selected_piece = board.de_select_piece()
                        use_power = False
                        if turn == 1:
                            text = ("It is Red's turn")
                        elif turn == 2:
                            text = ("It is Blue's turn")
                        else:
                            text = (f"Error with turn counter value: {turn}")
                    
                    if event.key == pygame.K_z:
                        if selected_piece == None:
                            text = ("No piece was selected")
                        elif selected_piece != None:
                            if selected_piece.power == None:
                                text = ("This piece has no power")
                            else:
                                if use_power:
                                    selected_piece.power.use(selected_piece, board)
                                    use_power = False
                                    selected_piece.power = None
                                    selected_piece = board.de_select_piece()
                                    turn_end = True
                                else:
                                    text = (f"Use: {selected_piece.power.description}? Confirm: Z Back: X")
                                    use_power = True


            
            if turn_end:
                if turn == 1:
                    turn = 2
                    text = ("It is Blue's turn")
                elif turn == 2:
                    turn = 1
                    text = ("It is Red's turn")
                else:
                    text = (f"Error with turn counter value: {turn}")     
                turn_end = False 
                chance = randint(1, spawn)
                if chance == 1:
                    board.spawn_power()
                    spawn = 5
                else:
                    spawn -= 1     

                self.give_power(board)
            board.draw(self.window, self.width, self.height, timer)
            font = pygame.font.Font(None, self.width // 20)
            text_center = (self.width // 2, self.height - (self.height // 22))
            text_surface = font.render(text, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.center = (text_center)
            self.window.blit(text_surface, text_rect)
            pygame.display.update()
            won = self.check_win(board)
            if won == 1 or won == 2:
                sleep(2)
                self.window.fill(BLACK)
                font = pygame.font.Font(None, 90)
                if won == 1:
                    text = (f"Red wins!")
                if won == 2:
                    text = (f"Blue wins!")
                text_surface = font.render(text, True, WHITE)
                text_rect = text_surface.get_rect()
                text_rect.center = (self.width// 2, self.height // 2)
                self.window.blit(text_surface, text_rect)
                pygame.display.update()
                sleep(3)
                running = False



    def run(self):
        running = True
        while running:
            self.clock.tick(self.fps)

            self.window.fill(BLACK)

            font = pygame.font.Font(None, self.width // 10)
            text = ("Welcome to Quadradius")
            text_surface = font.render(text, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.center = (self.width// 2, self.height // 3)
            self.window.blit(text_surface, text_rect)

            font = pygame.font.Font(None, self.width // 15)
            text = ("Start: Space Bar")
            text_surface = font.render(text, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.center = ((self.width // 3), (self.height // 3) * 2)
            self.window.blit(text_surface, text_rect)

            font = pygame.font.Font(None, self.width // 15)
            text = ("Quit: X")
            text_surface = font.render(text, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.center = ((self.width // 3) * 2, (self.height // 3) * 2)
            self.window.blit(text_surface, text_rect)


            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False

                if event.type == pygame.VIDEORESIZE:
                    self.width  = event.w
                    self.height  = event.h
                    self.window = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.run_game()

                    if event.key == pygame.K_x:
                        running = False

        pygame.quit
