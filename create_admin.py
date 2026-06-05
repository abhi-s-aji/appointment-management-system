import os
import django

# 1. Manually configure settings BEFORE any other imports
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_skills.settings')
django.setup()

# 2. Now it is safe to import models
from django.contrib.auth.models import User

# Create superuser if it doesn't exist
if not User.objects.filter(username='abhisaji').exists():
    User.objects.create_superuser('abhisaji', 'abhisaji@example.com', 'abhi2005')
    print("Admin user 'abhisaji' created successfully!")
else:
    print("Admin user 'abhisaji' already exists, skipping.")