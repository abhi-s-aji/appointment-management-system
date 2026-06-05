from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Sets up the admin user'

    def handle(self, *args, **options):
        user, created = User.objects.get_or_create(username='abhisaji')
        user.set_password('abhi2005')
        user.is_staff = True
        user.is_superuser = True
        user.save()
        if created:
            self.stdout.write("Admin user 'abhisaji' has been created.")
        else:
            self.stdout.write("Admin user 'abhisaji' password has been reset.")