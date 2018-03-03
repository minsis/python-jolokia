FROM python:3.6.4

# Source tree files
RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt -r dev-requirements.txt
