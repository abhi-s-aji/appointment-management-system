#!/bin/bash
set -e

# 1. Run Migrations
python manage.py migrate --noinput

# 2. Seed the Database
python manage.py shell -c "
import os
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

site = Site.objects.get_current()
site.domain = 'appointment-management-system-production-abhisaji.up.railway.app'
site.name = 'Appointment System'
site.save()

client_id = os.environ.get('GOOGLE_CLIENT_ID')
secret = os.environ.get('GOOGLE_CLIENT_SECRET')

if client_id and secret:
    app, _ = SocialApp.objects.update_or_create(
        provider='google',
        defaults={'name': 'Google', 'client_id': client_id, 'secret': secret}
    )
    app.sites.add(site)
"

# 3. Start Gunicorn
exec gunicorn django_skills.wsgi:application --bind 0.0.0.0:$PORT