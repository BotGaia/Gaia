from python:3.6-slim

run apt update && apt install -y git gcc make curl

run python -m pip install --upgrade pip

add ./requirements.txt /tmp

run pip install --upgrade pip && pip install -r /tmp/requirements.txt
run python -c "import nltk; nltk.download('stopwords');"

add ./bot /bot

workdir /bot
