from django.apps import AppConfig


class CakeUserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cake_user'

    def ready(self):
        import cake_user.signals.profile_creation_signal
