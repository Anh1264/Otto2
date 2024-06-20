from django.apps import AppConfig


class RobotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'robot'

    def ready(self):
        import robot.signals  # Import signals to connect them