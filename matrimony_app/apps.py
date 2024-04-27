from django.apps import AppConfig


class MatrimonyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'matrimony_app'

    def ready(self):
        import matrimony_app.signals