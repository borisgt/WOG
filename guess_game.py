import random

def generate_number(difficulty):
    """Generate a random number between 0 and the given difficulty level."""
    return random.randint(0, difficulty)

def get_guess_from_user(difficulty):
    """Prompt the user to guess a number within the specified range."""
    while True:
        user_input = input(f'Try to guess a number from 0 to {difficulty}:')
        if user_input.isdigit():
            user_number = int(user_input)
            if 0 <= user_number <= difficulty:
                return user_number
        print(f"Invalid input. Please enter a number between 0 and {difficulty}.")

def compare_results(random_number, user_number):
    """Compare the generated number with the user's guess."""
    return random_number == user_number

def play(difficulty):
    """Play the number guessing game with the specified difficulty level."""
    random_number = generate_number(difficulty)
    user_number = get_guess_from_user(difficulty)
    if compare_results(random_number, user_number):
        print("Congratulations! You guessed the correct number!")
    else:
        print(f"Sorry, the correct number was {random_number}. Better luck next time!")
