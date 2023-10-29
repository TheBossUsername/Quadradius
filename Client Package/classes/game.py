import pygame
from .constants import *
from .piece import Piece
from .square import Square
from .board import Board
from random import randint
from time import sleep
from .power import Power
from .server import Client

class Game:

    def __init__(self, server_ip, server_port):
        self.server = Client(server_ip, server_port)
        self.width = 800
        self.height = 800
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.window = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        pygame.display.set_caption('Quadradius')
        pygame.init()
        pygame.time.set_timer(pygame.USEREVENT, 100)

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
                    if len(piece.powers) >= 3:
                        del piece.powers[0]
                    piece.powers.append(square.power)
                    square.power = None
                


    def run_game(self):
        board = Board()

        your_turn = False
        spawn = 10
        use_power = False
        selected_piece = None
        selected_square = board.get_selected_square()
        turn = randint(1,2)
        timer = 0
        selected_power = None
        

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
                    
                if your_turn:
                    text = "It's your Turn"
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            if use_power:
                                pass
                            else:
                                selected_square = board.move_selected_square(selected_square, 1)

                        if event.key == pygame.K_RIGHT:
                            if use_power:
                                if selected_power < len(selected_piece.powers) - 1:
                                    selected_power += 1
                                    board.de_target_squares()
                                pass
                            else:
                                selected_square = board.move_selected_square(selected_square, 2)

                        if event.key == pygame.K_DOWN:
                            if use_power:
                                pass
                            else:
                                selected_square = board.move_selected_square(selected_square, 3)

                        if event.key == pygame.K_LEFT:
                            if use_power:
                                if selected_power > 0:
                                    selected_power -= 1
                                    board.de_target_squares()
                                pass
                            else:
                                selected_square = board.move_selected_square(selected_square, 4)

                        if event.key == pygame.K_SPACE:
                            if use_power:
                                pass
                            else:
                                if selected_piece == None:
                                    selected_piece = board.select_piece()
                                    if selected_piece == None:
                                        text = ("No piece was selected")
                                        selected_piece = board.de_select_piece()
                                    elif selected_piece.player == turn:
                                        if len(selected_piece.powers) != 0:
                                            text = (f"Move: Space bar, Powers: Z, Back: X")
                                        else:
                                            text = ("Move: Space bar, Back: X")
                                    elif selected_piece.player != turn:
                                        text = ("This piece is not yours!")
                                        selected_piece = board.de_select_piece()
                                    else:
                                        text = ("Error: Unknown thing selected")
                                        selected_piece = board.de_select_piece()
                                elif selected_piece != None:
                                    data = f"MOVE:{selected_piece.row}:{selected_piece.col}:{selected_square.row}:{selected_square.col}"
                                    self.server.send_player_input(data)     
                                    
                                        
                                else:
                                    text = ("ERROR with piece")

                        if event.key == pygame.K_x:
                            selected_piece = board.de_select_piece()
                            use_power = False
                            selected_power = None
                        
                        if event.key == pygame.K_z:
                            if selected_piece == None:
                                text = ("No piece was selected")
                            elif selected_piece != None:
                                if len(selected_piece.powers) == 0:
                                    text = ("This piece has no power")
                                else:
                                    if use_power:
                                        selected_piece.use_power(board, selected_power)
                                        use_power = False
                                        del selected_piece.powers[selected_power] 
                                        selected_power = None
                                        selected_piece = board.de_select_piece()
                                        end_turn = True
                                    else:
                                        selected_power = 0
                                        use_power = True
                else:
                    text = "Oppenent's Turn"

            print("Right before recieving data")
            data = self.server.recieve_server_update()
            print("Right after recieving data")
            if not data:
                break
            elif data == "NOT_LEGAL":
                text = ("That is not a legal move, Back: X")
            elif data == "MOVE":
                board.move_piece()
                selected_piece = board.de_select_piece()
            elif data == "END_TURN":
                your_turn = False
            elif data == "YOUR_TURN":
                your_turn = True

            


            if use_power:
                selected_piece.show_targets(selected_power, board)
            else:
                board.de_target_squares()
            

            
            if end_turn:
                chance = randint(1, spawn)
                if chance == 1:
                    board.spawn_power()
                    spawn = 10
                else:
                    spawn -= 1     

                self.give_power(board)
            board.draw(self.window, self.width, self.height, timer)
            if use_power:
                width_spacing = 2 + len(selected_piece.powers)
                for x in range(0, len(selected_piece.powers)):
                    text = (f"{selected_piece.get_power_name(x)}")
                    font = pygame.font.Font(None, self.width // (20  + (5 * (len(selected_piece.powers) - 1))))
                    text_center = (self.width * (x + 1) // width_spacing, self.height - (self.height // 22))
                    if x == selected_power:
                        text_surface = font.render(text, True, RED)
                    else:
                        text_surface = font.render(text, True, WHITE)
                    text_rect = text_surface.get_rect()
                    text_rect.center = (text_center)
                    self.window.blit(text_surface, text_rect)
                
                text = (f"Confirm: Z Back: X")
                font = pygame.font.Font(None, self.width // (20  + (5 * (len(selected_piece.powers) - 1))))
                text_center = (self.width * (width_spacing - 1) // width_spacing, self.height - (self.height // 22))
                text_surface = font.render(text, True, WHITE)
                text_rect = text_surface.get_rect()
                text_rect.center = (text_center)
                self.window.blit(text_surface, text_rect)
            else:
                font = pygame.font.Font(None, self.width // 20)
                text_center = (self.width // 2, self.height - (self.height // 22))
                text_surface = font.render(text, True, WHITE)
                text_rect = text_surface.get_rect()
                text_rect.center = (text_center)
                self.window.blit(text_surface, text_rect)
            print("Right before updating display")
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
