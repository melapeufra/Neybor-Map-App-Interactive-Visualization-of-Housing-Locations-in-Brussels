# Simple Dockerfile for the Neybor Flask app
FROM python:3.11-slim

# set workdir
WORKDIR /app

# copy requirements first for better caching
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# copy the application
COPY . /app

# expose port
EXPOSE 5000

# Use gunicorn for production-like server
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
