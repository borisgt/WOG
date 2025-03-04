FROM python:3.13.2-alpine

RUN apk add --no-cache \
    chromium \
    chromium-chromedriver \
    bash \
    curl \
    libstdc++ \
    nss \
    freetype \
    harfbuzz \
    ttf-freefont \
    dbus \
    tzdata

# Set environment variables for Chromium
ENV CHROMIUM_PATH=/usr/bin/chromium-browser
ENV CHROME_PATH=/usr/bin/chromium-browser
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# Set the display for headless mode
ENV DISPLAY=:99

WORKDIR /wog

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENV FLASK_PORT=8777

COPY main_score.py utils.py /wog/
COPY templates/ /wog/templates/

COPY Scores.txt /wog/Scores.txt
COPY ./tests/e2e.py /wog/tests/e2e.py

CMD [ "sh", "-c", "flask --app main_score.py run --host=0.0.0.0 --port=${FLASK_PORT}" ]