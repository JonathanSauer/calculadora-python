FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install pytest

CMD ["python", "calculator.py"]