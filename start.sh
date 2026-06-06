#!/bin/bash
set -e

# Run Migrations
python manage.py migrate --noinput

# Create superuser from Environment Variables
python manage.py shell -c "
import os
from django.contrib.auth import get_user_model

User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL')

if username and password and email:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print('Superuser created from environment variables.')
    else:
        print('Superuser already exists.')
else:
    print('WARNING: Superuser environment variables not set.')
"

# ... (Keep your SocialApp seeding logic here) ...

exec gunicorn django_skills.wsgi:application --bind 0.0.0.0:$PORT