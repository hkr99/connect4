import numpy as np
from Connect_Four import Connect_Four

def main():
    game = Connect_Four()
    while True:
        game.show_board()
        game.make_move()

        if game.check_win() == True:
            print("Player", game.player, "has won!")
            game.show_board()
            break
        else:
            pass

        game.player_switch()


main()