FROM python:3.15-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y libpq-dev

COPY . .

CMD ["python", "main.py"]