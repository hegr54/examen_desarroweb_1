from __future__ import unicode_literals

from django.conf import settings
from django.db import models

# Create your models here.

class Libro(models.Model):
    user    = models.ForeignKey(settings.AUTH_USER_MODEL)
    Nombre = models.CharField(max_length=120)
    Autor = models.CharField(max_length=120)
    Editorial = models.CharField(max_length=120)
    ISBN = models.CharField(max_length=120)
    precio = models.IntegerField()
    created = models.DateTimeField(auto_now = True)
    update  = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.Nombre)
