# Overview
Quadradius is a checkers like board game where you use your pieces to jump onto the opponents pieces to capture them. Expect there is added layer of strategy with randomly spawning power ups that can transform the board. Each square on the 8x8 board can be move up or down with the collected power ups, if a square gets too high pieces can not jump onto it, but any on top can jump down onto other pieces.

This is the local network version where you have one computer run the server package, and then 2 computers on the same wifi can connect and play against eachother.

[Software Demo Video](https://youtu.be/9tViORY3qOE)


# Network Communication

This uses a Client/Server architecture. On compputer hosts the server that controls the game, it recives input from the players and sends updates to thier games

It uses TCP and it uses the port 12345 but can be changed if needs be.

The fromt of the messages being sent are string files that then are decoded and broken into data like integers and strings

# Development Environment

I used Python to code the logic and the tool py.game to display it onto a screen and take input from a keyboard. I also used the libray random for the luck side of the game. I used the Socket library to send data from the server to the clients and back.


# Useful Websites

https://docs.python.org/
https://www.geeksforgeeks.org/socket-programming-python/

# Future Work

Speed up the procces of updating the boards