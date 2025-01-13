from memory_game import play as play_memory_game
from guess_game import play as play_guess_game
from currency_roulette_game import play as play_currency_roulette_game
from score import add_score

def welcome():
    user_name = input('What is your name:\n')
    print(f'Hi {user_name} and welcome to the World of Games: The Epic Journey\n')

def start_play():
    games = [
        'Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.',
        'Guess Game - guess a number and see if you chose like the computer.',
        'Currency Roulette - try and guess the value of a random amount of USD in ILS.'
    ]

    while True:
        print("Available games:")
        for num, game in enumerate(games, 1):
            print(f'{num}. {game}')

        game_input = input('Please choose a game by number (or type "exit" to quit):\n').strip().lower()
        if game_input == "exit":
            print("Exiting the game. Goodbye!")
            break
        elif game_input.isdigit() and 1 <= int(game_input) <= len(games):
            game_number = int(game_input)
            level_input = input('Please select a difficulty level (1-5):\n').strip()
            if level_input.isdigit() and 1 <= int(level_input) <= 5:
                level = int(level_input)
                print(f'Selected game: {games[game_number - 1]}')
                print(f'At difficulty level: {level}')

                selected_game = None
                if game_number == 1:
                    selected_game = play_memory_game
                elif game_number == 2:
                    selected_game = play_guess_game
                elif game_number == 3:
                    selected_game = play_currency_roulette_game

                if selected_game:
                    game_result = selected_game(level)
                    if game_result:
                        add_score(level)
                        print("Congrats! Victory is yours!")
                    else:
                        print("Sorry, you didn't win. Keep trying!")

                play_again = input("Do you want to play another game? (yes/no):\n").strip().lower()
                if play_again != 'yes':
                    print("Thank you for playing! Goodbye!")
                    break
            else:
                print('Invalid difficulty level selection. Please try again.')
        else:
            print('Invalid game selection. Please try again.')