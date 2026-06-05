#!/bin/bash
set -e

echo "--- STARTING DEPLOYMENT ---"
echo "GOOGLE_CLIENT_ID is set: $( [ -n "$GOOGLE_CLIENT_ID" ] && echo "YES" || echo "NO" )"

python manage.py migrate --noinput
python manage.py collectstatic --noinput

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
    print('SUCCESS: SocialApp configured.')
else:
    print('FAILURE: GOOGLE_CLIENT_ID or SECRET is empty in the environment!')
"

exec gunicorn django_skills.wsgi:application --bind 0.0.0.0:$PORT