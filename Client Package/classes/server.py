import socket

class Client:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip  
        self.server_port = server_port 
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((server_ip, server_port))
        self.client_socket.setblocking(False)
        

    def send_player_input(self, data):
        self.client_socket.send(data.encode())
        
    def recieve_server_update(self):
        try:
            server_data = self.client_socket.recv(1024).decode()
            return server_data
        except BlockingIOError:
            pass  # No data is available at the moment





