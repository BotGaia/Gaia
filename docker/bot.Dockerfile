FROM python:3.6-slim

RUN apt update && apt install -y git gcc make curl

RUN python -m pip install --upgrade pip

ADD ./requirements.txt /tmp

RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt
RUN python -c "import nltk; nltk.download('stopwords');"

ADD ./bot /bot

WORKDIR /bot

CMD make train && make run-telegram
