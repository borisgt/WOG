import os.path

from utils import SCORES_FILE_NAME

def add_score(difficulty):
    if type(difficulty) != type(0) or difficulty <= 0:
        print("Invalid difficulty level. Must be a positive integer.")
        return

    difficulty = int(difficulty)
    current_score = 0

    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, 'r') as score_file:
            file_content = score_file.read().strip()
            if file_content.isdigit():
                current_score = int(file_content)

    new_score = current_score + (difficulty * 3) + 5

    with open(SCORES_FILE_NAME, 'w') as score_file:
        score_file.write(str(new_score))
