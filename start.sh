#!/bin/bash
python manage.py migrate --noinput
python manage.py collectstatic --noinput

python manage.py shell -c "
import os
import sys
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

client_id = os.environ.get('GOOGLE_CLIENT_ID')
secret = os.environ.get('GOOGLE_CLIENT_SECRET')

if not client_id or not secret:
    print('ERROR: Environment variables GOOGLE_CLIENT_ID or GOOGLE_CLIENT_SECRET are missing!')
    sys.exit(1)

site, _ = Site.objects.update_or_create(
    id=1, 
    defaults={'domain': 'appointment-management-system-production-abhisaji.up.railway.app', 'name': 'Appointment System'}
)

app, _ = SocialApp.objects.update_or_create(
    provider='google',
    defaults={
        'name': 'Google',
        'client_id': client_id,
        'secret': secret
    }
)
app.sites.add(site)
"

gunicorn django_skills.wsgi:application --bind 0.0.0.0:$PORT