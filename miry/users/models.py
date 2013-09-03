from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

# Create your models here.

class mieszkanie(models.Model):
    preferencje = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey(User)

admin.site.register(mieszkanie)
