from classes.game import Game

server_ip = '0.0.0.0' # Put the IP address of the computer hosting the server
server_port = 12345 # Put the port the server is running on

def main(server_ip, server_port):
    game = Game(server_ip, server_port)
    game.run_game()

main(server_ip, server_port)