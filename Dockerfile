# Base image (slim to reduce vulnerabilities)
FROM python:3.11-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=8080
ENV DB_PORT=3306  

# Set working directory
WORKDIR /app

# Install system dependencies for MySQL client & Cloud SQL connections
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Copy the wait script and make it executable
COPY wait_for_cloudsql.sh /app/wait_for_cloudsql.sh
RUN chmod +x /app/wait_for_cloudsql.sh

# Expose the Cloud Run port
EXPOSE 8080

# Default command: wait for Cloud SQL, run migrations, then start Gunicorn
CMD ["/app/wait_for_cloudsql.sh"]
