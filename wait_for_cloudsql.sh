#!/bin/sh
# Cloud Run entrypoint for Django with non-blocking startup

set -e

DB_PORT=${DB_PORT:-3306}
echo "Checking Cloud SQL at $DB_HOST:$DB_PORT..."
nc -z $DB_HOST $DB_PORT && echo "Database reachable!" || echo "Database not reachable yet — continuing startup."

echo "Running migrations..."
python manage.py migrate || echo "Migration failed or DB not ready — continuing startup."

echo "Starting Gunicorn..."
exec gunicorn Work.wsgi:application --bind 0.0.0.0:${PORT:-8080} --workers 3
