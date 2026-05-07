#1/bin/bash

# Run migrations
python manage.py migrate

# Start gunicorn server
gunicorn AidanChiu_AI_Portfolio.wsgi:application --bind 0.0.0.0:8000