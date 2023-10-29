import socket
import threading
from classes.game import Game
import random
from classes.board import Board

# Server configuration
server_ip = '10.50.169.241'  # Use your server's IP address
server_port = 12345  # Choose a port for communication

# Create a socket to listen for incoming connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(2)  # Allow up to 2 players to connect

# List to store connected clients
clients = []
turn_counter = None
current_turn = None

def legal_move(selected_piece, selected_square, board):
        tq = selected_square
        sp = selected_piece
        sq = board.squares[sp.row][sp.col]
        tp = board.pieces[tq.row][tq.col]

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


def handle_client(client_socket, board):
    global turn_counter
    global current_turn
    global clients
    send_data = "YOUR_TURN"
    current_turn.send(send_data.encode()) 
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break

        elif client_socket == current_turn:
            message_parts = data.split(":", 1)
            if message_parts[0] == 'MOVE':
                piece_row = message_parts[1]
                piece_col = message_parts[2]
                square_row = message_parts[3]
                square_col = message_parts[4]
                selected_piece = board.pieces[piece_row][piece_col]
                selected_square = board.squares[square_row][square_col]
                if legal_move(selected_piece, selected_square, board):
                    board.move(selected_piece, selected_square)
                    send_data = "MOVE"
                    client_socket.send(send_data.encode())
                    send_data = "END_TURN"
                    current_turn.send(send_data.encode())
                    turn_counter += 1
                    current_turn = clients[turn_counter % 2]
                    send_data = "YOUR_TURN"
                    current_turn.send(send_data.encode())    
                else:
                    send_data = "NOT_LEGAL"
        
        
        client_socket.send(send_data.encode())
            

def main():
    global turn_counter
    global current_turn
    global clients
    print(f"Server listening on {server_ip}:{server_port}")

    while len(clients) < 2:
        print("waiting")
        client, addr = server_socket.accept()
        clients.append(client)
        print(f"Connected to {addr[0]}:{addr[1]}")
    board = Board()

    print(f"Starting Now")
    turn_counter = random.randint(1,2)
    print(f"Turn Counter: {turn_counter}")
    current_turn = clients[turn_counter % 2]
    print(f"Current Turn: {current_turn}")

    for client in clients:
        client_handler = threading.Thread(target=handle_client, args=(client, board))
        client_handler.start()

if __name__ == "__main__":
    main()
