# Entry point to script, runs game loop
from connect_four import ConnectFour

def main():
    game = ConnectFour()
    game_over = False

    while not game_over:
        game.print_board()

        # Get player's move
        col = int(input(f"\nPlayer {game.current_player}'s turn. Choose a column (1-7): ")) - 1
        # Find the row, make the move and check for win condition
        last_move = game.make_move(col)
        if last_move is not False and game.check_win(last_move, col):
            game_over = True
            game.print_board()
            print(f"\nPlayer {game.current_player} wins!")
            break
        game.player_switch()

if __name__ == "__main__":
    print('Game Starting, get ready!\n')
    main()