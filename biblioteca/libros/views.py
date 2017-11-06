# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from .forms import LibroModelForm
from .mixin import FormUserNeededMixin
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Libro
# Create your views here.
def home_libros(request):
    print request
    v = "Desde home libros"
    v1="Rigoberto"
    v2 = "Usuario: "+v1
    return render(request, "home.html", {'v':v, 'v2':v2})

class LibroCreateView(LoginRequiredMixin,FormUserNeededMixin,CreateView):
    form_class = LibroModelForm
    template_name = "crearlibro_view.html"
    success_url = "/libros/lista"
    login_url = "/admin"

class LibroUpdateView(UpdateView):
    queryset = Libro.objects.all()
    form_class = LibroModelForm
    template_name = "Actualizar_view.html"
    success_url = "/libros/lista"

class LibroDeleteView(LoginRequiredMixin, DeleteView):
    model = Libro
    template_name = "Delete_confirm.html"
    success_url = reverse_lazy("libro_lista")

class LibroListView(ListView):
    template_name = "lista_libros.html"

    def get_queryset(self, *args, **kwargs):
        qs = Libro.objects.all()
        print self.request.GET
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
            Q(Nombre__icontains=query)|
            Q(user__username__icontains=query)
            )
        return qs
    def get_context_data(self, *args, **kwargs):
         context = super(LibroListView, self).get_context_data(*args, **kwargs)
         print context
         context['create_form'] = LibroModelForm()
         context['create_url'] = reverse_lazy("libro_lista")
         return context

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
