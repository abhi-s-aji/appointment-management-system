import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_skills.settings')
django.setup()

from django.contrib.auth.models import User

try:
    user = User.objects.get(username='abhisaji')
    user.set_password('abhi2005')
    user.save()
    print("Password reset successful!")
except User.DoesNotExist:
    print("User 'abhisaji' not found.")