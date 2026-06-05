#!/bin/bash
python manage.py migrate --noinput
python manage.py collectstatic --noinput

python manage.py shell -c "
import os
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

# Debug: Print the environment variables to the logs
print(f'DEBUG: GOOGLE_CLIENT_ID is {os.environ.get('GOOGLE_CLIENT_ID')}')

site, _ = Site.objects.update_or_create(
    id=1, 
    defaults={'domain': 'appointment-management-system-production-abhisaji.up.railway.app', 'name': 'Appointment System'}
)

app, _ = SocialApp.objects.update_or_create(
    provider='google',
    defaults={
        'name': 'Google',
        'client_id': os.environ.get('GOOGLE_CLIENT_ID'),
        'secret': os.environ.get('GOOGLE_CLIENT_SECRET')
    }
)
app.sites.add(site)
"

gunicorn django_skills.wsgi:application --bind 0.0.0.0:$PORT