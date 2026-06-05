#!/bin/bash
set -e

# Run Migrations and Static Collection
python manage.py migrate --noinput
python manage.py collectstatic --noinput

# Seed the database
python manage.py shell -c "
import os
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

# Get or create the site object
site = Site.objects.get_current()
site.domain = 'appointment-management-system-production-abhisaji.up.railway.app'
site.name = 'Appointment System'
site.save()

# Create or update the social app
client_id = os.environ.get('GOOGLE_CLIENT_ID')
secret = os.environ.get('GOOGLE_CLIENT_SECRET')

if client_id and secret:
    app, _ = SocialApp.objects.update_or_create(
        provider='google',
        defaults={
            'name': 'Google',
            'client_id': client_id,
            'secret': secret
        }
    )
    app.sites.add(site)
    print('Google SocialApp configured successfully.')
else:
    print('WARNING: GOOGLE_CLIENT_ID or SECRET not found in environment.')
"

exec gunicorn django_skills.wsgi:application --bind 0.0.0.0:$PORT