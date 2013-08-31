from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.

class Kurs(models.Model):
    osoby = models.ManyToManyField(User, null=True, blank=True)
    nazwa = models.CharField(max_length=255)
    opis = models.TextField(null=True)
    miejsca = models.IntegerField()

    def __unicode__(self):
        return self.nazwa

    def wolne(self):
        return (self.miejsca - len(self.osoby.all()))

admin.site.register(Kurs)


