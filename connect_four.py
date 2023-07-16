# Script containing all the logic of connect four game
import numpy as np
import sys
import pygame
class ConnectFour:
    def __init__(self, rows=6, cols=7):
        # Initialise a default game state
        self.board = np.zeros((rows,cols))
        # We'll be using player 1 to start for now, both players denoted by 1 and 2
        self.current_player = 1

    def start_game(self):
        # If I want to start a new game using the same board size as initially created when class instantiated
        rows, cols = self.board.shape
        self.board = np.zeros((rows, cols))
        self.current_player = 1

    # def end_game(self):
    #     # end current game
    #     sys.exit()

    def print_board(self):
        # Simple print, I notice online people are doing a flip but this won't be necessary if we populate our board from
        # bottom to top
        print(self.board)

# game = ConnectFour()
# game.print_board()

print("You can do it, keep going!")