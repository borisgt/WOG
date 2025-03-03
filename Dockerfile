FROM python:3.13.2-alpine

WORKDIR /wog

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENV FLASK_PORT=8777

COPY main_score.py utils.py /wog/
COPY templates/ /wog/templates/

COPY Scores.txt /wog/Scores.txt
COPY ./tests/e2e.py /wog/tests/e2e.py

CMD [ "sh", "-c", "flask --app main_score.py run --host=0.0.0.0 --port=${FLASK_PORT}" ]