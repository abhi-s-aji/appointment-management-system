from django.apps import AppConfig
from django.db.models.signals import post_migrate

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

    def ready(self):
        # This will run automatically after migrations are finished
        post_migrate.connect(self.setup_admin)

    def setup_admin(self, **kwargs):
        from django.contrib.auth.models import User
        user, created = User.objects.get_or_create(username='abhisaji')
        user.set_password('abhi2005')
        user.is_staff = True
        user.is_superuser = True
        user.save()
        print("Admin user 'abhisaji' has been created/updated via signal.")