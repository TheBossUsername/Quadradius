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
        self.server = Client(server_ip, server_port) # Make client socket
        self.width = 800
        self.height = 800
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.window = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE) # Make window
        pygame.display.set_caption('Quadradius')
        pygame.init()
        pygame.time.set_timer(pygame.USEREVENT, 100) # Timer for animated power orbs
        
    def give_power(self, piece, square):
        if len(piece.powers) >= 3:
            del piece.powers[0]
        piece.powers.append(square.power)
        square.power = None        


    def run_game(self): 

        board = Board() # Make player board
        your_turn = False 
        use_power = False # Variable to lock input when selecting powers
        selected_piece = None 
        selected_square = board.get_selected_square() # Highlighted square to move and select
        turn = 1 # Turn counter 
        timer = 0 # Timer for animated power orbs
        selected_power = None
        won = 0 # Variable for who won

        # Intitialize text at the bottom
        if turn == 1:
            text = ("It is Red's Turn")
        elif turn == 2:
            text = ("It is Blue's Turn")
        else:
            text = (f"Turn error turn : {turn}")
        

        running = True
        while running:
            self.clock.tick(self.fps)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.VIDEORESIZE: # Updates window when resized
                    self.width  = event.w
                    self.height  = event.h
                    self.window = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

                if event.type == pygame.USEREVENT: # Adds 1 to timer each second
                    timer += 1   
                
                if event.type == pygame.KEYDOWN:
                    # Moves the selected square unless selecting powers
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
                    
                    if your_turn: # Check if it is your turn
                        if event.key == pygame.K_SPACE:
                            if use_power:
                                pass
                            else:
                                if selected_piece == None: # If no piece selected, select piece
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
                                elif selected_piece != None: # If piece already selected, attempt to move it to selected square
                                    data = f"MOVE:{selected_piece.row}:{selected_piece.col}:{selected_square.row}:{selected_square.col}"
                                    self.server.send_player_input(data)        
                                else:
                                    text = ("ERROR with piece")

                        if event.key == pygame.K_x: # Back out and deselect piece
                            selected_piece = board.de_select_piece()
                            use_power = False
                            selected_power = None
                            if turn == 1:
                                text = ("It is Red's Turn")
                            elif turn == 2:
                                text = ("It is Blue's Turn")
                            else:
                                text = (f"Turn error turn : {turn}")
                        
                        if event.key == pygame.K_z: # Open pieces power menu, or use selecte power
                            if selected_piece == None:
                                text = ("No piece was selected")
                            elif selected_piece != None:
                                if len(selected_piece.powers) == 0:
                                    text = ("This piece has no power")
                                else:
                                    if use_power:
                                        data = f"USE:{selected_piece.row}:{selected_piece.col}:{selected_power}"
                                        self.server.send_player_input(data)
                                    else:
                                        selected_power = 0
                                        use_power = True
                    else:
                        if turn == 1:
                            text = ("It is Red's Turn")
                        elif turn == 2:
                            text = ("It is Blue's Turn")
                        else:
                            text = (f"Turn error turn : {turn}")

            data = self.server.recieve_server_update() # Receive update from server
            if data == None:
                pass
            elif data == "NOT_LEGAL":
                text = ("That is not a legal move, Back: X")
            elif "MOVE" in data: # This piece moved, update player board
                message_parts = data.split(":")
                piece_row = message_parts[1]
                piece_col = message_parts[2]
                square_row = message_parts[3]
                square_col = message_parts[4]
                selected_piece = board.pieces[int(piece_row)][int(piece_col)]
                sq = board.squares[int(square_row)][int(square_col)]
                board.move_piece(selected_piece, sq)
                selected_piece = board.de_select_piece()
                # Change turn
                if turn == 1:
                    turn = 2
                elif turn == 2:
                    turn = 1
            elif data == "END_TURN": # Stop sending input
                your_turn = False
                if turn == 1:
                    text = ("It is Red's Turn")
                elif turn == 2:
                    text = ("It is Blue's Turn")
                else:
                    text = (f"Turn error turn : {turn}")
            elif data == "YOUR_TURN": # Allow input to be sent
                your_turn = True
                if turn == 1:
                    text = ("It is Red's Turn")
                elif turn == 2:
                    text = ("It is Blue's Turn")
                else:
                    text = (f"Turn error turn : {turn}")
            elif "SPAWN" in data: # Update board with spawned power
                message_parts = data.split(":")
                square_row = message_parts[1]
                square_col = message_parts[2]
                type = message_parts[3]
                board.spawn_power(int(square_row), int(square_col), int(type))
            elif "GIVE" in data: # Give piece this power
                message_parts = data.split(":")
                piece_row = message_parts[1]
                piece_col = message_parts[2]
                square_row = message_parts[3]
                square_col = message_parts[4]
                sp = board.pieces[int(piece_row)][int(piece_col)]
                sq = board.squares[int(square_row)][int(square_col)]
                self.give_power(sp, sq)
            elif "USE" in data: # Use power from selected piece
                message_parts = data.split(":")
                piece_row = message_parts[1]
                piece_col = message_parts[2]
                type = message_parts[3]
                sp = board.pieces[int(piece_row)][int(piece_col)]
                sp.use_power(board, int(type))
                use_power = False
                del sp.powers[int(type)] 
                selected_power = None
                selected_piece = board.de_select_piece()
                if turn == 1:
                    turn = 2
                elif turn == 2:
                    turn = 1
            elif data == "RED_WINS": 
                won = 1
            elif data == "BLUE_WINS":
                won = 2


            


            if use_power:
                selected_piece.show_targets(selected_power, board) # Show what the power will affect
            else:
                board.de_target_squares() 
            
            board.draw(self.window, self.width, self.height, timer) # draw the board
            # Write text to the bottom
            if use_power: # If selecting a power
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

            pygame.display.update()

            if won == 1 or won == 2: # If someone won display winner and quit
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
