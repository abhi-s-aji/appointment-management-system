#!/bin/bash
set -e

# Log the presence of variables
echo "--- DEBUG LOGS ---"
if [ -z "$GOOGLE_CLIENT_ID" ]; then echo "MISSING: GOOGLE_CLIENT_ID"; else echo "FOUND: GOOGLE_CLIENT_ID"; fi
if [ -z "$GOOGLE_CLIENT_SECRET" ]; then echo "MISSING: GOOGLE_CLIENT_SECRET"; else echo "FOUND: GOOGLE_CLIENT_SECRET"; fi

python manage.py migrate --noinput
python manage.py collectstatic --noinput

# Seed the database
python manage.py shell -c "
import os
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

client_id = os.environ.get('GOOGLE_CLIENT_ID')
secret = os.environ.get('GOOGLE_CLIENT_SECRET')

if client_id and secret:
    site = Site.objects.get_current()
    site.domain = 'appointment-management-system-production-abhisaji.up.railway.app'
    site.name = 'Appointment System'
    site.save()

    app, _ = SocialApp.objects.update_or_create(
        provider='google',
        defaults={'name': 'Google', 'client_id': client_id, 'secret': secret}
    )
    app.sites.add(site)
"

exec gunicorn django_skills.wsgi:application --bind 0.0.0.0:$PORT