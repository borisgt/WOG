import random
import time
from utils import screen_cleaner

def generate_sequence(difficulty):
    """
    Generates a list of random numbers between 1 and 101, with a length equal
    to the difficulty.
    """
    return [random.randint(1, 101) for _ in range(difficulty)]

def get_list_from_user(difficulty):
    """
    Asks the user to input a list of numbers matching the length of the
    generated sequence.
    """

    while True:
        user_input = input(f"Enter {difficulty} numbers, separated by spaces: ")
        user_numbers = user_input.split()

        if len(user_numbers) == difficulty and all(num.isdigit() for num in user_numbers):
            return list(map(int, user_numbers))
        else:
            print(f"Please enter exactly {difficulty} valid numbers separated by spaces.")


def is_list_equal(generated_sequence, user_numbers):
    """ Compares the generated sequence with the user's input """
    return generated_sequence == user_numbers

def play(difficulty):
    """
    Runs the memory game by generating a sequence of random numbers, showing
    them briefly, and asking the user to recall the sequence. Returns True if
    the user's input matches the sequence, otherwise False.
    """
    sequence = generate_sequence(difficulty)
    print(f"Memorize this sequence: {sequence}")
    time.sleep(1)  # Wait for 1 second before clearing the screen
    screen_cleaner()  # Clears the screen

    user_numbers = get_list_from_user(difficulty)
    is_correct = is_list_equal(sequence, user_numbers)

    if is_correct:
        print("Great! You remembered the sequence correctly!")
        return True
    else:
        print(f"Oops! The correct sequence was: {sequence}")
        return False