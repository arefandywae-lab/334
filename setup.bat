@echo off
echo =======================================
echo Django Project Setup Script (Windows)
echo =======================================

echo 1. Creating Virtual Environment...
python -m venv .venv

echo 2. Activating Virtual Environment...
call .venv\Scripts\activate

echo 3. Installing Requirements...
pip install -r requirements.txt
if errorlevel 1 (
    echo pip install failed! Using default Django installation.
    pip install django
)

echo 4. Applying Migrations...
python manage.py makemigrations
python manage.py migrate

echo 5. Starting Development Server...
echo The server is starting. Press Ctrl+C to stop.
python manage.py runserver

pause
