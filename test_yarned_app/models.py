from django.db import models

class User(models.Model):      
      name=models.CharField(max_length=50)
      surname=models.CharField(max_length=100)
      bio=models.CharField(max_length=300)

class Contact(models.Model):      
      userId=models.IntegerField()
      ctype=models.CharField(max_length=10)
      value=models.CharField(max_length=100)

