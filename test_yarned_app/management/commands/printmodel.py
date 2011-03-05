from django.core.management.base import BaseCommand
from django.db import models
from django.conf import settings
from django.utils.importlib import import_module


class Command(BaseCommand):
    help = 'Prints all project models and the count of objects in every model'

    def handle(self, **options):
        for app in settings.INSTALLED_APPS:
            cur_app = import_module(app + '.models')
            cur_app_models = models.get_models(cur_app)
            self.stdout.write('Model:%s \n' % cur_app.__name__)
            for item_model in cur_app_models:
                name = item_model._meta.object_name
                count = item_model.objects.all().count()
                self.stdout.write('     %s %d \n' % (name, count))
                self.stderr.write('     error: %s %d \n' % (name, count))
