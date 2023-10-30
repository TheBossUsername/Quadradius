from classes.game import Game

server_ip = '0.0.0.0' # Put the IP address of the computer hosting the server
server_port = 12345 # Put A port to use, 12345 is usually open. Do not use anything under 1023

def main(server_ip, server_port):
    game = Game(server_ip, server_port) # Intitialize the game server
    game.run()

main(server_ip, server_port)