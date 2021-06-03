from django.apps import AppConfig


class ImagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'images'
    
    def ready(self):
        #import signal handlersn to register our signals
        import images.signals
