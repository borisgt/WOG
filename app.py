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

        game_number = None
        while game_number is None:
            game_input = input('Please choose a game by number (or 0 to exit):\n')
            if game_input.isdigit():
                game_number = int(game_input)
                if 0 <= game_number <= len(games):
                    break
            game_number = None
            print('Invalid game selection.')

        if game_number == 0:
            print("Exiting the game. Goodbye!")
            return

        level = None
        while level is None:
            level_input = input('Please select a difficulty level (1-5) or 0 to exit:\n')
            if level_input.isdigit():
                level = int(level_input)
                if 0 <= level <= 5:
                    break
            level = None
            print('Invalid level selection.')

        if level == 0:
            print("Exiting the game. Goodbye!")
            return

        print(f'Selected game: {games[game_number - 1]}')
        print(f'At difficulty level: {level}')
        return
