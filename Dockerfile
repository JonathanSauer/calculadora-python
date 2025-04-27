FROM python:3.10-slim

WORKDIR /app

COPY calculadora.py .
COPY main.py .

CMD ["python", "main.py"]