import threading
import random
from .board import Board
import time
from .server import Server

class Game:
    def __init__(self, server_ip, server_port):

        self.server = Server(server_ip, server_port) # Make a server class
        self.board = Board() # Make a master board that will keep track of everything
        self.clients = [] # List of clients
        self.turn_counter = None # A counter to keep track of who's turn it is
        self.current_turn = None # A variable that hold the current players socket
        self.spawn = 7 # A 1 out of spawn chance to put a power on the board, lower number, more powers per turn

    def legal_move(self, selected_piece, selected_square): # Check if the player can move it's piece there
            tq = selected_square
            sp = selected_piece
            sq = self.board.squares[sp.row][sp.col]
            tp = self.board.pieces[tq.row][tq.col]

            if tq.row >= 0 and tq.col >= 0 and tq.row < 8 and tq.col < 8: # check if the target square is somehow out of the board
                if 3 not in sp.traits: # If piece does not have the climb trait, check if target square is too high
                    if (tq.height - sq.height) >= 2:
                        return False
                
                if tp != None: # Check if it is going to jump onto another piece
                    if tp.player == sp.player: # Check if it is thier own piece
                        return False
                    if 2 in tp.traits: # Check if target piece has jump proof
                        return False
                
                # If the square is adjecent return True
                if (tq.row, tq.col) == (sp.row + 1, sp.col):
                    return True
                elif (tq.row, tq.col) == (sp.row - 1, sp.col):
                    return True
                elif (tq.row, tq.col) == (sp.row, sp.col + 1):
                    return True
                elif (tq.row, tq.col) == (sp.row, sp.col - 1):
                    return True
                elif 4 in sp.traits: # If piece has move diagonally and target square is diagnol return true
                    if (tq.row, tq.col) == (sp.row + 1, sp.col + 1):
                        return True
                    elif (tq.row, tq.col) == (sp.row - 1, sp.col + 1):
                        return True
                    elif (tq.row, tq.col) == (sp.row - 1, sp.col - 1):
                        return True
                    elif (tq.row, tq.col) == (sp.row + 1, sp.col - 1):
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False # Otherwise reuturn false
            

    def give_power(self): # Check if a piece is on a square with a power, then give that piece it's power
        for row in range(8): # Check every square for a power
            for col in range(8):
                square = self.board.squares[row][col]
                piece = self.board.pieces[row][col]
                if square.power != None and piece != None:
                    if len(piece.powers) >= 3:
                        del piece.powers[0]
                    piece.powers.append(square.power)
                    square.power = None
                    send_data = f"GIVE:{piece.row}:{piece.col}:{square.row}:{square.col}"
                    for c in self.clients:
                        self.server.send_server_data(c, send_data) # update player's boards
                    time.sleep(1)

    def check_win(self): # Check if somone has won
            pieces_1 = 0
            pieces_2 = 0
            for row in range(8):
                for col in range(8):
                    piece = self.board.pieces[row][col]
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



    def run_game(self, client_socket):
        while True:
            data = self.server.recieve_player_input(client_socket) # Wait for input
            if not data: # Check if there is no data
                pass
            elif client_socket == self.current_turn: # Check if it is this players turn
                message_parts = data.split(":") # Split the message up into seperate data. First word is either MOVE or USE
                if message_parts[0] == 'MOVE': # Move the piece
                    piece_row = message_parts[1]
                    piece_col = message_parts[2]
                    square_row = message_parts[3]
                    square_col = message_parts[4]
                    selected_piece = self.board.pieces[int(piece_row)][int(piece_col)]
                    selected_square = self.board.squares[int(square_row)][int(square_col)]
                    if self.legal_move(selected_piece, selected_square): # Check if the piece can go there
                        # Store data to send to payers that the piece has moved
                        send_data = f"MOVE:{selected_piece.row}:{selected_piece.col}:{selected_square.row}:{selected_square.col}" 
                        self.board.move_piece(selected_piece, selected_square) # Move the piece on the master board
                        for c in self.clients: # Send data to all players
                            self.server.send_server_data(c, send_data)
                        time.sleep(1) # Sleeps so the sent data does not get joined together
                        send_data = "END_TURN" # End the current players turn to prevent more input
                        self.current_turn.send(send_data.encode()) 
                        time.sleep(1)
                        chance = random.randint(1, self.spawn) 
                        if chance == 1: # Check if power should be spawned
                            row, col, type = self.board.spawn_power() #Spawn power and return info to send
                            send_data = f"SPAWN:{row}:{col}:{type}" 
                            for c in self.clients: # Update players boards with power
                                self.server.send_server_data(c, send_data)
                            self.spawn = 7 # Reset the chance 
                        else:
                            self.spawn -= 1 # Increase the chance of power spawning
                        time.sleep(1)
                        self.give_power() # Give powers to pieces
                        self.turn_counter += 1 
                        self.current_turn = self.clients[self.turn_counter % 2] # Change who's turn it is
                        send_data = "YOUR_TURN" # Let new player send input
                        self.server.send_server_data(self.current_turn, send_data)
                        time.sleep(1)    
                        win = self.check_win() # Check if somebody won
                        if win == 0:
                            pass
                        elif win == 1:
                            send_data = f"RED_WINS"
                            for c in self.clients:
                                self.server.send_server_data(c, send_data)
                        elif win == 2:
                            send_data = f"BLUE_WINS"
                            for c in self.clients:
                                self.server.send_server_data(c, send_data) 
                        
                    else: # If peice can not move there send message saying so
                        send_data = "NOT_LEGAL"
                        client_socket.send(send_data.encode())

                elif message_parts[0] == 'USE': # Use pieces power
                    piece_row = message_parts[1]
                    piece_col = message_parts[2]
                    index = message_parts[3] 
                    selected_piece = self.board.pieces[int(piece_row)][int(piece_col)]
                    send_data = f"USE:{selected_piece.row}:{selected_piece.col}:{index}" 
                    selected_piece.use_power(self.board, int(index)) # Use the power on the master board
                    del selected_piece.powers[int(index)] 
                    for c in self.clients:
                            self.server.send_server_data(c, send_data) # Use the power on the player's boards
                    time.sleep(1)
                    send_data = "END_TURN"
                    self.current_turn.send(send_data.encode())
                    time.sleep(1)
                    chance = random.randint(1, self.spawn)
                    if chance == 1:
                        row, col, type = self.board.spawn_power()
                        send_data = f"SPAWN:{row}:{col}:{type}"
                        for c in self.clients:
                            self.server.send_server_data(c, send_data)
                        self.spawn = 10
                    else:
                        self.spawn -= 1    
                    time.sleep(1)
                    self.give_power()
                    self.turn_counter += 1
                    self.current_turn = self.clients[self.turn_counter % 2]
                    send_data = "YOUR_TURN"
                    self.server.send_server_data(self.current_turn, send_data)
                    time.sleep(1)
                    win = self.check_win()
                    if win == 0:
                        pass
                    elif win == 1:
                        send_data = f"RED_WINS"
                        for c in self.clients:
                            self.server.send_server_data(c, send_data)
                    elif win == 2:
                        send_data = f"BLUE_WINS"
                        for c in self.clients:
                            self.server.send_server_data(c, send_data)
                    

                    

                        
            
            
                

    def run(self):
        print(f"Server listening on {self.server.server_ip}:{self.server.server_port}")
        while len(self.clients) < 2: # Wait till 2 players join
            print("waiting")
            client, addr = self.server.server_socket.accept()
            self.clients.append(client)
            print(f"Connected to {addr[0]}:{addr[1]}")

        self.turn_counter = random.randint(1,2)
        self.current_turn = self.clients[self.turn_counter % 2] 
        send_data = "YOUR_TURN" # Send a initial your turn to the chosen player
        self.server.send_server_data(self.current_turn, send_data)
        
        for client in self.clients: # Start a handler for each player
            client_handler = threading.Thread(target=self.run_game, args=(client,))
            client_handler.start()
