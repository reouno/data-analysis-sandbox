FROM python:3.9.10

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y \
    && apt-get install -y postgresql-client netcat

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# run entrypoint.dev.sh
ENTRYPOINT ["/usr/src/app/entrypoint.dev.sh"]