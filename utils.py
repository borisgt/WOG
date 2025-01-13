import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = 113

def screen_cleaner():
    """
    Clears the terminal screen. Works on Windows and Unix-like systems.
    Handy for resetting the screen before a new game begins or during
    gameplay, like in Memory Game.
    """
    os.system('cls' if os.name == 'nt' else 'clear')