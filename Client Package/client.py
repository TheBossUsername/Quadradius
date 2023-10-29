import socket
import pygame
from classes.board import Board
from classes.game import Game

# Server configuration
server_ip = '10.50.169.241'  # Use the IP address of the server
server_port = 12345  # Use the same port as the server

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, server_port))

def send_player_input(data):
    client_socket.send(data.encode())


def main():
    width = 800
    height = 800
    clock = pygame.time.Clock()
    fps = 60
    window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
    pygame.display.set_caption('Quadradius')
    pygame.init()
    pygame.time.set_timer(pygame.USEREVENT, 100)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    send_player_input('UP')
                    
            if event.type == pygame.VIDEORESIZE:
                width  = event.w
                height  = event.h
                window = pygame.display.set_mode((width, height), pygame.RESIZABLE)

if __name__ == "__main__":
    main()





