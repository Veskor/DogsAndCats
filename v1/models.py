from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cat(models.Model):
    name = models.CharField(max_length=32)
    birthday = models.DateField()
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.name

class Dog(models.Model):
    name = models.CharField(max_length=32)
    birthday = models.DateField()
    owner = models.ForeignKey(User)

    def __str__(self):
        return self.name
