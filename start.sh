#!/usr/bin/env bash
set -o errexit

# Run migrations
python manage.py migrate

# Prepare static assets for Render/WhiteNoise
python manage.py collectstatic --no-input

# Start gunicorn server
gunicorn portfolio_project.wsgi:application --bind 0.0.0.0:${PORT:-8000}

