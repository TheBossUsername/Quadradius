import threading
import random
from .board import Board
import time
from .server import Server

class Game:
    def __init__(self, server_ip, server_port):

        self.server = Server(server_ip, server_port)
        self.board = Board()
        self.clients = []
        self.turn_counter = None
        self.current_turn = None
        self.spawn = 7

    def legal_move(self, selected_piece, selected_square):
            tq = selected_square
            sp = selected_piece
            sq = self.board.squares[sp.row][sp.col]
            tp = self.board.pieces[tq.row][tq.col]

            if tq.row >= 0 and tq.col >= 0 and tq.row < 8 and tq.col < 8:
                if 3 not in sp.traits:
                    if (tq.height - sq.height) >= 2:
                        return False
                
                if tp != None:
                    if tp.player == sp.player:
                        return False
                    if 2 in tp.traits:
                        return False
                
                    
                if (tq.row, tq.col) == (sp.row + 1, sp.col):
                    return True
                elif (tq.row, tq.col) == (sp.row - 1, sp.col):
                    return True
                elif (tq.row, tq.col) == (sp.row, sp.col + 1):
                    return True
                elif (tq.row, tq.col) == (sp.row, sp.col - 1):
                    return True
                elif 4 in sp.traits:
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
                return False
            

    def give_power(self):
        for row in range(8):
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
                        self.server.send_server_data(c, send_data)
                    time.sleep(1)

    def check_win(self):
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
            data = self.server.recieve_player_input(client_socket)
            if not data:
                pass
            elif client_socket == self.current_turn:
                message_parts = data.split(":")
                if message_parts[0] == 'MOVE':
                    piece_row = message_parts[1]
                    piece_col = message_parts[2]
                    square_row = message_parts[3]
                    square_col = message_parts[4]
                    selected_piece = self.board.pieces[int(piece_row)][int(piece_col)]
                    selected_square = self.board.squares[int(square_row)][int(square_col)]
                    if self.legal_move(selected_piece, selected_square):
                        send_data = f"MOVE:{selected_piece.row}:{selected_piece.col}:{selected_square.row}:{selected_square.col}"
                        self.board.move_piece(selected_piece, selected_square)
                        for c in self.clients:
                            self.server.send_server_data(c, send_data)
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
                            self.spawn = 7
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
                        
                    else:
                        send_data = "NOT_LEGAL"
                        client_socket.send(send_data.encode())

                elif message_parts[0] == 'USE':
                    piece_row = message_parts[1]
                    piece_col = message_parts[2]
                    type = message_parts[3]
                    selected_piece = self.board.pieces[int(piece_row)][int(piece_col)]
                    send_data = f"USE:{selected_piece.row}:{selected_piece.col}:{type}"
                    selected_piece.use_power(self.board, int(type))
                    del selected_piece.powers[int(type)] 
                    for c in self.clients:
                            self.server.send_server_data(c, send_data)
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
        while len(self.clients) < 2:
            print("waiting")
            client, addr = self.server.server_socket.accept()
            self.clients.append(client)
            print(f"Connected to {addr[0]}:{addr[1]}")

        self.turn_counter = random.randint(1,2)
        self.current_turn = self.clients[self.turn_counter % 2]
        send_data = "YOUR_TURN"
        self.server.send_server_data(self.current_turn, send_data)
        
        for client in self.clients:
            client_handler = threading.Thread(target=self.run_game, args=(client,))
            client_handler.start()
