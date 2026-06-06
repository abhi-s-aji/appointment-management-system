#!/bin/bash
set -e

echo "--- STARTING DEPLOYMENT ---"

# 1. Database Migrations
python manage.py migrate --noinput

# 2. Collect Static Files
python manage.py collectstatic --noinput

# 3. Create Superuser and Setup Google SocialApp
python manage.py shell -c "
import os
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

# Create Superuser
User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

if username and password and email:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print('Superuser created successfully.')
    else:
        print('Superuser already exists.')

# Setup Google SocialApp
client_id = os.environ.get('GOOGLE_CLIENT_ID')
secret = os.environ.get('GOOGLE_CLIENT_SECRET')

if client_id and secret:
    site = Site.objects.get_current()
    site.domain = 'appointment-management-system-production-abhisaji.up.railway.app'
    site.name = 'Appointment System'
    site.save()

    app, created = SocialApp.objects.update_or_create(
        provider='google',
        defaults={'name': 'Google', 'client_id': client_id, 'secret': secret}
    )
    app.sites.add(site)
    print('Google SocialApp configured.')
"

# 4. Start Gunicorn
echo "Starting Gunicorn..."
exec gunicorn django_skills.wsgi:application --bind 0.0.0.0:$PORT