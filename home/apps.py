from django.apps import AppConfig
from django.db.models.signals import post_migrate

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

    def ready(self):
        post_migrate.connect(self.setup_admin)

    def setup_admin(self, **kwargs):
        from django.contrib.auth.models import User
        # Check if user exists, if not, create it
        user, created = User.objects.get_or_create(username='abhisaji')
        if created:
            user.is_staff = True
            user.is_superuser = True
            # Set a placeholder password that the user MUST change
            user.set_unusable_password() 
            user.save()
            print("Admin user 'abhisaji' created. Please use 'python manage.py createsuperuser' to set a password.")