#!/usr/bin/env bash
set -o errexit

# Run migrations
python manage.py migrate

# Start gunicorn server
gunicorn portfolio_project.wsgi:application --bind 0.0.0.0:${PORT:-8000}


