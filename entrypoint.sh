#!/bin/bash
echo "Running migrations..."
python manage.py makemigrations
python manage.py migrate 
echo "Starting the server..."
python manage.py runserver 0.0.0.0:8000