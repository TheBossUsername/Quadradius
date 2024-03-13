# Quadradius
## History
Quadradius was a browser game that was released in 2007 by Jimmi Heiserman based on his 1995 High School project which was called "Squares". Jimmi created a new version in Flash, with Brad Kayal providing the graphics. It has since been discontinued in the 2010s and sadly has not been released since.  

## Gameplay
Quadradius is a game that is similar to checkers. The objective of the game is to capture all your opponent's pieces by landing on them. You can only move to adjacent squares and not diagonally. However, what makes the game unpredictable are the power-ups that randomly spawn on the board. These can be acquired by landing a piece on them. The powers are randomized and can enable a piece to do various things such as moving diagonally, destroying pieces around it, and teleporting. But the most interesting powers are those that alter the elevation of squares on the board. A piece can move up one tier like climbing stairs, but if it is two or more tiers above the square they are on they cannot move there. This adds a layer of strategy to the game, allowing players to trap their opponent's pieces and create walls or moats to control the battlefield.

## Restoration
Playing this game was a big part of my childhood and it introduced me to strategy games as a whole. However, when I searched for it as an adult, I was saddened to see that it no longer existed. In an attempt to relieve some nostalgia, I decided to recreate the game as best as I could using Python.

# My Version of Quadradius
This is an local multiplayer version that you can play with a friend on the same network. It does not have online multiplayer at this moment.

## Tools Used
I used the libraries Pygame and Sockets. The processes are organized into classes and employ parallel processing with threads.

## How to Play
### Requirements
- At least 2 computers. (Or if you don't mind seeing each other's screens just one that has enough processing power.)
- A IDE like Visual Studio Code.

### Set Up
1. Download the packages on both computers.
2. Open the main file in the server package in an IDE and edit the IP address to yours. [How to find my IP address](https://www.theverge.com/23351435/ip-address-how-to-find-macos-windows-ios-android-iphone)
3. Run the server main file.
4. On the 2 computers you want to use, open the main file in the client package in an IDE and edit the IP address to match the computer that is running the game server, the one you used in step 2. (If you are running the server and playing the game on the same computer you will have to run the client file in another terminal)
5. If you see the game window pop up on both computers and say whose turn it is you are good to go! 
6. To play again, close and run all the files with the same settings

### Controls
1. Use the arrow keys to move your blue selector over your piece.
2. Use the spacebar to select your piece, it should be highlighted. 
3. Move and select a square adjacent to your piece and it will move. 
4. If your piece has a power it will glow green and prompt you to press Z to view your powers when the piece is selected

### Rules
- You can not move to a square that is 2 tiers above your square. (Unless you have the flight power)
- You can not jump onto a jumpproof piece, they can only be captured with powers