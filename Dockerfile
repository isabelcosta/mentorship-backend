  
FROM python:3.6.8-alpine

LABEL mentorship-backend flask api

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD python run.py