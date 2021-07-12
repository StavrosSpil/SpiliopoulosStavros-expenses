from django.apps import AppConfig


class BuildingsConfig(AppConfig):
    name = 'buildings'

    def ready(self):
        import buildings.signals