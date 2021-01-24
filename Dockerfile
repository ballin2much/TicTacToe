FROM python:3
COPY code/ code/
WORKDIR /code/
CMD ["python", "app.py"]