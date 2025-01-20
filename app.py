from memory_game import play as play_memory_game
from guess_game import play as play_guess_game
from currency_roulette_game import play as play_currency_roulette_game
from score import add_score

def welcome():
    """Greets the user and asks for their name."""
    user_name = input('What is your name:\n')
    print(f'Hi {user_name} and welcome to the World of Games: The Epic Journey\n')

def start_play():
    """Main function to display game options, handle user input, and start selected games."""

    # List of available games with descriptions
    games = [
        'Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.',
        'Guess Game - guess a number and see if you chose like the computer.',
        'Currency Roulette - try and guess the value of a random amount of USD in ILS.'
    ]

    # Corresponding game functions
    game_play_functions = [play_memory_game, play_guess_game, play_currency_roulette_game]

    while True:
        print("Available games:")
        for num, game in enumerate(games, 1):
            print(f'{num}. {game}')

        # Get user input for game selection
        game_input = input('Please choose a game by number (or type "exit" to quit):\n').strip().lower()

        # Handle exit command
        if game_input == "exit":
            print("Exiting the game. Goodbye!")
            break

        # Validate game selection
        elif game_input.isdigit() and 1 <= int(game_input) <= len(games):
            game_number = int(game_input)

            # Ensure valid difficulty level selection
            while True:
                level_input = input('Please select a difficulty level (1-5):\n').strip()
                if level_input.isdigit() and 1 <= int(level_input) <= 5:
                    level = int(level_input)
                    break   # Exit if valid level is selected
                print('Invalid difficulty level selection. Please try again.')

            print(f'Selected game: {games[game_number - 1]}')
            print(f'At difficulty level: {level}')

            # Play the selected game
            game_result = game_play_functions[game_number - 1](level)

            # If the game was won, add points
            if game_result:
                add_score(level)

            # Ask if the user wants to play another game
            play_again = input("\nDo you want to play another game? (y/n):").strip().lower()
            if play_again != 'y':
                print("Thank you for playing! Goodbye!")
                break
        else:
            print('Invalid game selection. Please enter a valid number.')