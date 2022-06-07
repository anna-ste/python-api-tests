FROM python:3.7-slim-buster

COPY entrypoint.sh /usr/local/bin
RUN chmod 755 /usr/local/bin/entrypoint.sh

RUN  apt-get update
RUN apt-get install -y wget unzip default-jre default-jdk

COPY . /tests
WORKDIR /tests

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

ENV API_KEY="MpX1Tuy5OM5ufv9x9+nk4YGtSTVbje5gqWfTwUE7x4kZfyaAeItyNSDW"
ENV API_SECRET="44Cz+wrcuaZQaOot0/V6FsjlG55GdDRGJWJJHqxhzeQ6xpmxHcwPfe+krtytGmdAZZiiYYtkwTof1l1490CjNQ=="
ENV OTP="9X-5rE9h4VAz3kc"

RUN wget https://github.com/allure-framework/allure2/releases/download/2.13.8/allure-2.13.8.zip
RUN unzip allure-2.13.8.zip

EXPOSE 8080

ENTRYPOINT ["entrypoint.sh"]