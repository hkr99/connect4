import numpy as np
from numpy import argmax

class Connect_Four:
    def __init__(self):
        self.board = np.zeros((6,7))
        self.player = 1
        self.move_number = 1

    def show_board(self):
        print(np.flip(self.board, 0))

    def make_move(self):
        print("Player ", self.player," take your turn.\n This is move number ", self.move_number, ".")
        self.col = int(input("Please enter a column number between 1 and 7: "))-1
        if self.is_valid_move(self.col) == True:
            self.move_number = self.move_number+1
            self.row = np.argmax(self.board[:,self.col]==0)
            self.board[self.row,self.col] = self.player
        else:
            print("Invalid move, try again.")

    def is_valid_move(self, col):
        return (self.board[:,self.col]==0).any()

    def player_switch(self):
        self.player = 1 if self.player == 2 else 2

    def check_win(self):
        if self.move_number >= 7:
            win_list = [self.player, self.player, self.player, self.player]
            # Horizontal check
            for i in range(max(0, self.col-3), min(self.col+3, 7)):
                if self.board[self.row, i:i+4].tolist() == win_list:
                    return True
            # Vertical check
            for i in range(max(0, self.row-3), min(self.row+3, 6)):
                if self.board[i:i+4, self.col].tolist() == win_list:
                    return True
                
            # Diagonal check (\ direction)
            #for irow, icol in zip(range(max(0, self.row-3), min(self.row+3, 7)), range(max(0, self.col-3), min(self.col+3, 6))):
                #if [self.board[irow+i, icol+i] for i in range(4)] == win_list:
                   # return True

            # Diagonal check (/ direction)
            #for irow, icol in zip(range(max(0, self.row-3), min(self.row+3, 7)), range(max(0, self.col-3), min(self.col+3, 6))):
                #if [self.board[irow-i, icol+i] for i in range(4)] == win_list:
                    #return True
                
            # Diagonal check (\ direction)
            start_row = max(self.row - min(self.row, self.col, 3), 0)
            start_col = max(self.col - min(self.row, self.col, 3), 0)
            if start_row + 3 < 6 and start_col + 3 < 7:
                if [self.board[start_row + i, start_col + i] for i in range(4)] == win_list:
                    return True

            # Diagonal check (/ direction)
            start_row = min(self.row + min(6 - self.row, min(self.col, 3)), 5)
            start_col = max(self.col - min(6 - self.row, min(self.col, 3)), 0)
            if start_row - 3 >= 0 and start_col + 3 < 7:
                if [self.board[start_row - i, start_col + i] for i in range(4)] == win_list:
                    return True
        else:
            return False
