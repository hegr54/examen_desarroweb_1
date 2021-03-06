# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from .validators import validate_content
# Create your models here.

class Libro(models.Model):
    user    = models.ForeignKey(settings.AUTH_USER_MODEL)
    Nombre = models.CharField(max_length=50, validators=[validate_content])
    Autor = models.CharField(max_length=50, validators=[validate_content])
    Editorial = models.CharField(max_length=150, validators=[validate_content])
    ISBN = models.CharField(max_length=50, validators=[validate_content])
    precio = models.IntegerField( validators=[validate_content])
    created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(self.Nombre)
