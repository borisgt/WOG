FROM python:3.13.2-alpine

WORKDIR /wog

RUN apk update && apk add --no-cache \
    firefox \
    wget \
    unzip \
    curl \
    && rm -rf /var/cache/apk/*

# Install GeckoDriver
RUN GECKO_DRIVER_VERSION=$(curl -sS https://api.github.com/repos/mozilla/geckodriver/releases/latest | grep 'tag_name' | cut -d\" -f4) \
    && wget -O /tmp/geckodriver.tar.gz https://github.com/mozilla/geckodriver/releases/download/$GECKO_DRIVER_VERSION/geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz \
    && tar -xzf /tmp/geckodriver.tar.gz -C /usr/local/bin \
    && rm /tmp/geckodriver.tar.gz \

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENV FLASK_PORT=8777

COPY main_score.py utils.py /wog/
COPY templates/ /wog/templates/

COPY Scores.txt /wog/Scores.txt
COPY ./tests/e2e.py /wog/tests/e2e.py

CMD [ "sh", "-c", "flask --app main_score.py run --host=0.0.0.0 --port=${FLASK_PORT}" ]