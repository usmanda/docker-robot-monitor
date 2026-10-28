FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY battery_monitor.py .

CMD ["python", "battery_monitor.py"]