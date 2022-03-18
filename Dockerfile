FROM python:3.9

ADD . /app

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./start.sh /app/start.sh

RUN chmod +x /app/start.sh

COPY ./app /app

WORKDIR /app

CMD ["/app/start.sh"]