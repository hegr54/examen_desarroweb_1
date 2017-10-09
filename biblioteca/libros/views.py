# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def home_libros(request):
    print request
    v = "Desde home libros"
    v1="Rigoberto"
    v2 = "Usuario: "+v1
    return render(request, "home.html", {'v':v, 'v2':v2})
