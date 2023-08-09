FROM python:latest

RUN apt-get update && apt-get install -y gcc

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app

CMD python bot.py
