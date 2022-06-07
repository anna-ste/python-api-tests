                                                                        FROM python:3.7-slim-buster
RUN  apt-get update \
  && apt-get install -y wget


RUN apt-get install default-jre -y
RUN apt-get install default-jdk -y
RUN apt-get install unzip

COPY . /tests
WORKDIR /tests


COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


RUN wget https://github.com/allure-framework/allure2/releases/download/2.13.8/allure-2.13.8.zip
RUN unzip allure-2.13.8.zip
EXPOSE 8080

ENV API_KEY="MpX1Tuy5OM5ufv9x9+nk4YGtSTVbje5gqWfTwUE7x4kZfyaAeItyNSDW"
ENV API_SECRET="44Cz+wrcuaZQaOot0/V6FsjlG55GdDRGJWJJHqxhzeQ6xpmxHcwPfe+krtytGmdAZZiiYYtkwTof1l1490CjNQ=="
ENV OTP="9X-5rE9h4VAz3kc"

ENTRYPOINT ["behave",  "-f", "allure", "-o", "reports", "-f", "pretty"]
ENTRYPOINT ["/tests/allure-2.13.8/bin/allure serve --port 8080 reports"]
