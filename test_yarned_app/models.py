from django.db import models
from django.contrib.auth.models import User


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
