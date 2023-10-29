import socket
import threading
from classes.game import Game
import random

# Server configuration
server_ip = '10.50.169.241'  # Use your server's IP address
server_port = 12345  # Choose a port for communication

# Create a socket to listen for incoming connections
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(2)  # Allow up to 2 players to connect

# List to store connected clients
clients = []
current_turn = None

def handle_client(client_socket):
    global current_turn
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break

        if client_socket == current_turn:
            # Process player input
            if data == 'UP':
                print("Player pushed up")
            

def main():
    print(f"Server listening on {server_ip}:{server_port}")

    while len(clients) < 2:
        print("waiting")
        client, addr = server_socket.accept()
        clients.append(client)
        print(f"Connected to {addr[0]}:{addr[1]}")

    current_turn = random.choice(clients)

    for client in clients:
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

if __name__ == "__main__":
    main()
