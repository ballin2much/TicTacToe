FROM python:3
COPY . code/
WORKDIR /code/
RUN pip install numpy