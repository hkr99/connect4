# Entry point to script, runs game loop
from connect_four import ConnectFour

def main():
    # Create a new game
    game = ConnectFour()
    # Start the game
    game.start_game()

    while True:
        # Main game loop
        # Get the current state of the game
        # Display the state
        # Get the player's move
        # Apply the move
        # Check for win condition
        pass

    while not game.is_game_over():
        # Main game loop
        # Get the current state of the game
        # Display the state
        # Get the player's move
        # Apply the move
        # Check for win condition
        pass



if __name__ == "__main__":
    main()
