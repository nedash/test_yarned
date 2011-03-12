from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models.signals import post_save, post_delete
from django.conf import settings


class Person(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(blank=True, max_length=100)
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)


class Contact(models.Model):
    person = models.ForeignKey(Person, null=True)
    ctype = models.CharField(max_length=10)
    value = models.CharField(blank=True, max_length=300)

    def __unicode__(self):
        return u"%s for %s" % (self.ctype, self.value)


class RequestSnapShot(models.Model):
    user = models.ForeignKey(User, null=True)
    path = models.CharField(max_length=150)
    priority = models.IntegerField(default=0)


class OperationLog(models.Model):
    obj_type = models.CharField(max_length=20)
    op_object = models.IntegerField()
    operation = models.CharField(max_length=20)
    date = models.DateTimeField(default=datetime.now())


operation_type = {True: 'create', False: 'edit', None: 'delete'}


def crud_postprocessor(sender, instance, **kwargs):
    if instance._meta.object_name not in settings.SIGNAL_SKIP_OBJECTS:
        #print instance._meta.object_name #kwargs
        OperationLog.objects.create(
                     obj_type=instance._meta.object_name,
                     op_object=instance.id,
                     operation=operation_type[kwargs.get('created', None)])


post_save.connect(crud_postprocessor)
post_delete.connect(crud_postprocessor)
