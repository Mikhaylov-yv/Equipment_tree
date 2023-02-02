FROM python:3.10.8-slim
WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN pip install --proxy http://10.11.36.32:3128 --upgrade pip
COPY ./requirements.txt .
RUN apt update && \
    apt -y install libpq-dev gcc && \
    pip install --proxy http://10.11.36.32:3128 -r requirements.txt
COPY ./src .