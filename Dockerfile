FROM python:3.6

RUN pip install rasa_nlu[spacy] && \
    python -m spacy download pt

RUN pip install rasa_nlu[tensorflow]

RUN mkdir /Gaia

ADD . /Gaia

WORKDIR /Gaia

CMD python train.py all