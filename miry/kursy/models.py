from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.

class Termin(models.Model):
    date = models.DateTimeField()

    def __unicode__(self):
        return str(self.date)

class Kurs(models.Model):
    osoby = models.ManyToManyField(User, null=True, blank=True)
    nazwa = models.CharField(max_length=255)
    opis = models.TextField(null=True)
    miejsca = models.IntegerField()
    termin = models.ForeignKey(Termin)
    miejsce = models.CharField(max_length=255, null=True, blank=True)

    def __unicode__(self):
        return self.nazwa

    def wolne(self):
        return (self.miejsca - len(self.osoby.all()))

admin.site.register(Kurs)
admin.site.register(Termin)


