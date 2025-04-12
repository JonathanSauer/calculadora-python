FROM python:3.10-slim

WORKDIR /app

COPY calculator.py .
COPY main.py .

CMD ["python", "main.py"]