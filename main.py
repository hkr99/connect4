# Entry point to script, runs game loop
from connect_four import ConnectFour
from render import Piece
import pygame

cell_size = 100;

def main():
    game = ConnectFour()
    screen = game.create_window()
    running = True
    myfont = pygame.font.SysFont("monospace", 75)

    static_pieces = pygame.sprite.Group()
    moving_pieces = pygame.sprite.Group()
    screen_height = cell_size * (game.board.shape[0] + 1)

    while running:
        pygame.time.delay(100) 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.end_game()

            if event.type == pygame.MOUSEBUTTONDOWN:

                x, y = pygame.mouse.get_pos()
                col = x // cell_size
                last_move = game.make_move(col)
                game.print_board()

                spawn_pos = game.get_last_token_position(col, cell_size)
                piece = Piece(pos=(spawn_pos[0] + cell_size // 2, 0))  # at the top of the column
                piece.add_to_group(static_pieces, moving_pieces)
                piece.draw_player_colour(game.current_player)

                if last_move is not False and game.check_win(last_move,col):

                    pygame.display.set_caption(f"Player {game.current_player} wins!")
                    label = myfont.render(f"Player {game.current_player} wins!", 1, (255, 255, 0))
                    screen.blit(label, (40, 10))
                    pygame.display.flip()
                    pygame.time.wait(3000)
                    running = False

                game.player_switch()

        for piece in moving_pieces:
            piece.piece_movement(screen_height)

        # screen.fill((255, 255, 255))
        game.draw_board(screen)
        moving_pieces.draw(screen)
        static_pieces.draw(screen)
        pygame.display.flip()
    # pygame.quit()

if __name__ == "__main__":
    print('Game Starting, get ready!\n')
    main()

# def main():
#     game = ConnectFour()
#     game_over = False
#
#     while not game_over:
#         game.print_board()
#
#         # Get player's move
#         col = int(input(f"\nPlayer {game.current_player}'s turn. Choose a column (1-7): ")) - 1
#         # Find the row, make the move and check for win condition
#         last_move = game.make_move(col)
#         if last_move is not False and game.check_win(last_move, col):
#             game_over = True
#             game.print_board()
#             print(f"\nPlayer {game.current_player} wins!")
#             break
#         game.player_switch()
