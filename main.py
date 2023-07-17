import numpy as np
from Connect_Four import Connect_Four

def main():
    game = Connect_Four()
    while True:
        game.show_board()
        game.make_move()

        if game.check_win() == True:
            game.show_board()
            print("Player", game.player, "has won!")
            break
        else:
            pass

        game.player_switch()


main()
