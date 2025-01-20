import random
import requests

def get_money_interval(difficulty):
    """Fetches the USD to ILS exchange rate and calculates the acceptable range for guessing."""

    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')

    if response.status_code != 200:     # Check if request was successful
        print("Could not fetch exchange rate. Please try again later.")
        return None, None, None

    exchange_rate = response.json().get('rates', {}).get('ILS', None)

    if exchange_rate is None:  # Check if the exchange rate exists in response
        print("Exchange rate unavailable. Please try again later.")
        return None, None, None

    random_usd = random.randint(1, 100)
    converted_ils = random_usd * exchange_rate

    margin = 10 - difficulty
    min_value = converted_ils - margin
    max_value = converted_ils + margin

    return min_value, max_value, random_usd

def get_guess_from_user(random_usd):
    """Asks the user to guess the ILS value of a given USD amount."""
    user_float = input(f"\nHow much is {random_usd} USD in ILS? ").strip()
    """Check if the input is a valid float."""
    is_float = user_float.replace('.', '', 1).isdigit() and user_float.count('.') <= 1

    while not is_float:
        user_float = input("Invalid input. Please enter a valid number: ").strip()

    return float(user_float)

def compare_results(guess, min_value, max_value):
    """Checks if the guess is in the allowed range."""
    return min_value <= guess <= max_value

def play(difficulty):
    """Runs the currency roulette game and returns True if the user wins."""

    min_value, max_value, random_usd = get_money_interval(difficulty)

    if min_value is None or max_value is None:
        return False

    user_guess = get_guess_from_user(random_usd)

    if compare_results(user_guess, min_value, max_value):
        print(f"Great job! {user_guess} ILS is correct.")
        return True
    else:
        print(f"Oops! {user_guess} ILS is wrong.")
        print(f"The correct range was {min_value:.2f} - {max_value:.2f} ILS.")
        return False