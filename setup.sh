#!/bin/bash
echo "======================================="
echo "Django Project Setup Script (Mac/Linux)"
echo "======================================="

echo "1. Creating Virtual Environment..."
python3 -m venv .venv

echo "2. Activating Virtual Environment..."
source .venv/bin/activate

echo "3. Installing Requirements..."
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
else
    echo "requirements.txt not found, installing django..."
    pip install django
fi

echo "4. Applying Migrations..."
python manage.py makemigrations
python manage.py migrate

echo "5. Starting Development Server..."
echo "The server is starting. Press Ctrl+C to stop."
python manage.py runserver
