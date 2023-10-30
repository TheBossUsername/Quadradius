import socket

class Server:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip  
        self.server_port = server_port 
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((server_ip, server_port))
        self.server_socket.listen(2)  # Allow up to 2 players to connect
        

    def send_server_data(self, client, data):
        client.send(data.encode())
        
    def recieve_player_input(self, client):
        data = client.recv(1024).decode()
        return data