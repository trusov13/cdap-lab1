FROM python:3.10-slim

WORKDIR /app

RUN useradd -u 1000 appuser

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN mkdir -p /home/appuser && chmod -R 777 /home/appuser

RUN chown -R appuser:appuser /app

USER appuser

CMD ["python", "app.py"]