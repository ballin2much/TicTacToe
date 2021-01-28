FROM python:3
ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0
WORKDIR /app
COPY requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
# run gunicorn

RUN adduser -D user
USER user

CMD gunicorn hello_django.wsgi:application --bind 0.0.0.0:$PORT