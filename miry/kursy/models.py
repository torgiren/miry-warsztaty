from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Kurs(models.Model):
    osoby = models.ManyToManyField(User)
    nazwa = models.CharField(max_length=255)
    opis = models.TextField(null=True)
