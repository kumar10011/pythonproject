FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install flask

EXPOSE 80

CMD ["python", "app.py"]
