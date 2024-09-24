FROM python:3.9-slim

WORKDIR /app
COPY main.py .
COPY input.txt .

CMD ["python", "main.py"]