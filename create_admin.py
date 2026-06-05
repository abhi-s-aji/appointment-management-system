import os
import django
from django.contrib.auth.models import User

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_skills.settings')
django.setup()

# Create superuser if it doesn't exist
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'yourpassword123')
    print("Admin user created successfully!")
else:
    print("Admin user already exists, skipping.")