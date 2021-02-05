FROM python:3.9.1-alpine3.12

MAINTAINER Akash Patel

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN apk add bash

CMD ["./wait-for-it.sh","messaging:5672","-t","60","--","./run.sh"]

