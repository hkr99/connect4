# Script containing all the logic of connect four game
import numpy as np
import sys
import pygame


class ConnectFour:
    def __init__(self, rows=6, cols=7):
        # Initialise a default game state
        self.board = np.zeros((rows, cols))
        # We'll be using player 1 to start for now, both players denoted by 1 and 2
        self.current_player = 1
        self.turn = 1

    def start_game(self):
        # If I want to start a new game using the same board size as initially created when class instantiated
        rows, cols = self.board.shape
        self.board = np.zeros((rows, cols))
        self.current_player = 1

    def end_game(self):
        # end current game
        sys.exit()

    def print_board(self):
        # Simple print, I notice online people are doing a flip but this won't be necessary if we populate our board from
        # bottom to top
        print("\n", self.board)

    def create_window(self, cell_size=100):
        pygame.init()
        width = cell_size * int(self.board.shape[1])
        height = cell_size * int(self.board.shape[0]+1)  # Extra row of space for text/hover

        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Connect Four | Hif n Ish')
        return screen

    def draw_board(self, screen, cell_size=100):
        radius = int(cell_size / 2 - 5)
        screen_height = cell_size * self.board.shape[0]
        blue = (0, 0, 255)
        black = (0, 0, 0)

        for row in range(self.board.shape[0]):
            for col in range(self.board.shape[1]):
                pygame.draw.rect(screen, blue, (col * cell_size, row * cell_size+cell_size, cell_size, cell_size))
                pygame.draw.circle(screen, black, (int(col*cell_size+cell_size/2), int(row*cell_size+cell_size+cell_size/2)), radius)
                
    #def draw_board(self, screen, cell_size=100):
        #radius = int(cell_size / 2 - 5)
        #screen_height = cell_size * self.board.shape[0]
        #blue = (0, 0, 255)
        #black = (0, 0, 0)
        #red = (255, 0, 0)
        #yellow = (255, 255, 0)
        #for row in range(self.board.shape[0]):
            #for col in range(self.board.shape[1]):
                #pygame.draw.rect(screen, blue, (col * cell_size, row * cell_size+cell_size, cell_size, cell_size))
                #pygame.draw.circle(screen, black, (int(col*cell_size+cell_size/2), int(row*cell_size+cell_size+cell_size/2)), radius)

        #for row in range(self.board.shape[0]):
            #for col in range(self.board.shape[1]):
                #if self.board[row][col] == 1:
                    #pygame.draw.circle(screen, red, (int(col*cell_size+cell_size/2), int((row + 1.5) * cell_size)), radius)
                #elif self.board[row][col] == 2:
                    #pygame.draw.circle(screen, yellow,
                                       #(int(col*cell_size+cell_size/2), int((row + 1.5) * cell_size)),
                                       #radius)
    def is_valid_move(self, col):
        # A move is considered valid if 1. column exists within range; 2. the top row of that column is empty
        # this will check whether column is full
        return self.board[0][col] == 0

    def make_move(self, col):
        # Checks for move validity
        if col < 0 or col > 6:
            print("Please make sure to enter a number between 1 and 7")
            return False

        if not self.is_valid_move(col):
            print("Invalid move, column is full, please try again")
            return False

        # Maybe argmax methodology is better but I chose different route to have interesting conversation
        # This will give the next row in said column that is open
        for row in reversed(range(self.board.shape[0])):
            if self.board[row][col] == 0:
                self.board[row][col] = self.current_player
                self.turn += 1
                return row

    def player_switch(self):
        # Small arithmetic trick to make sure the player switching works, more maths than coding logic
        self.current_player = 3 - self.current_player
    
    def get_last_token_position(self, col, cell_size):
        # Returns the top position of the last token in the given column in pixels
        for row in range(self.board.shape[0]):
            if self.board[row][col] != 0:
                return col * cell_size, (row + 1) * cell_size  # Pixel position

    # Now we do win checking, a win can only happen from last piece placed so instead of scanning the board
    # we've decided to check the vicinity from the last placed piece
    # This also helps with how I populate my board, as a regular scan would mess with the indexing badly
    # Instead, it does it from last placed piece for better logic
    def horizontal_check(self, row, col):
        count = 1  # Count the piece itself

        # Check to the left
        i = col - 1
        while i >= 0 and self.board[row][i] == self.current_player:
            count += 1
            i -= 1

        # Check to the right
        i = col + 1
        while i < self.board.shape[1] and self.board[row][i] == self.current_player:
            count += 1
            i += 1
        # Evaluate to true using this conditional
        return count >= 4

    def vertical_check(self, row, col):
        count = 1  # Count piece itself
        # Checking downwards as pieces fall down, you cannot have a win "upwards"
        # from the last placed piece
        i = row + 1
        while i < self.board.shape[0] and self.board[i][col] == self.current_player:
            count += 1
            i += 1
        return count >= 4

    def asc_diagonal_check(self, row, col):
        count = 1  # Count the piece itself

        # Check bottom-left
        i, j = row + 1, col - 1
        while i < self.board.shape[0] and j >= 0 and self.board[i][j] == self.current_player:
            count += 1
            i += 1
            j -= 1

        # Check top-right
        i, j = row - 1, col + 1
        while i >= 0 and j < self.board.shape[1] and self.board[i][j] == self.current_player:
            count += 1
            i -= 1
            j += 1

        return count >= 4

    def desc_diagonal_check(self, row, col):
        count = 1

        # Check top-left
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0 and self.board[i][j] == self.current_player:
            count += 1
            i -= 1
            j -= 1

        # Check bottom-left
        i, j = row + 1, col + 1
        while i < self.board.shape[0] and j < self.board.shape[1] and self.board[i][j] == self.current_player:
            count += 1
            i += 1
            j += 1

        return count >= 4

    def check_win(self, row, col):
        if self.turn >= 7:
            return (self.horizontal_check(row, col) or
                    self.vertical_check(row, col) or
                    self.asc_diagonal_check(row, col) or
                    self.desc_diagonal_check(row, col))
        else:
            return False

# game = ConnectFour()
# game.print_board()
