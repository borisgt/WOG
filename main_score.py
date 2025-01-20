from flask import Flask, render_template
import os
from utils import SCORES_FILE_NAME, BAD_RETURN_CODE

app = Flask(__name__)
@app.route("/")

def score_server():
    if os.path.exists(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, 'r') as score_file:
            score = score_file.read().strip()
            if score.isdigit():
                return render_template('score.html', score=score)

    return render_template('error.html', error=BAD_RETURN_CODE)

if __name__ == '__main__':
    app.run()