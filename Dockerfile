FROM python:3.8

WORKDIR  /SentimentAnalysis

ADD . /SentimentAnalysis

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "main.py"]