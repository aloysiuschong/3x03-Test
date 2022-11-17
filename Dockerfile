FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENV FLASK_ENV=development
ENV FLASK_APP=main.py

COPY . .

CMD [ "python3", "main.py"]
