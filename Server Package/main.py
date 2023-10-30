from classes.game import Game

server_ip = '10.50.169.241' # Put the IP address of the computer hosting the server
server_port = 12345 # Put the port the server is running on

def main(server_ip, server_port):
    game = Game(server_ip, server_port)
    game.run()

main(server_ip, server_port)