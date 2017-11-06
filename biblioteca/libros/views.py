# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .forms import LibroModelForm
from .mixin import FormUserNeededMixin

from .models import Libro
# Create your views here.
def home_libros(request):
    print request
    v = "Desde home libros"
    v1="Rigoberto"
    v2 = "Usuario: "+v1
    return render(request, "home.html", {'v':v, 'v2':v2})

class LibroCreateView(FormUserNeededMixin,CreateView):
    form_class = LibroModelForm
    template_name = "crearlibro_view.html"
    success_url = "/libros/lista"



def libros_lista_libros(request):
    result_set = Libro.objects.all()
    context = {
    "result": result_set
    }
    return render(request, "lista_libros.html", context)

def libros_detalle_libro(request, id=10):
    result_set = Libro.objects.get(id=id)
    context = {
    "result": result_set
    }
    return render(request, "detalle_libro.html", context)
