# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Libro
# Create your views here.
def home_libros(request):
    print request
    v = "Desde home libros"
    v1="Rigoberto"
    v2 = "Usuario: "+v1
    return render(request, "home.html", {'v':v, 'v2':v2})


def lista_libros(request):
    result_set = Libro.objects.all()
    context = {
    "result": result_set
    }
    return render(request, "lista_libros.html", context)

def detalle_libro(request, id=10):
    result_set = Libro.objects.get(id=id)
    context = {
    "result": result_set
    }
    return render(request, "detalle_libro.html", context)
