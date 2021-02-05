FROM node:15.7.0-alpine3.10

MAINTAINER AKASH PATEL

WORKDIR /app

COPY ./package.json /app

RUN npm install 

COPY . /app

EXPOSE 3000

CMD ["npm", "run","dev"]
