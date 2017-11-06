"""biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import home
from libros.views import home_libros , libros_lista_libros, libros_detalle_libro,LibroListView
from libros.views import LibroCreateView, LibroUpdateView,LibroDeleteView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^libros/$', home_libros, name='home_libros'),
    url(r'^libros/detalle/(?P<id>\d+)/$', libros_detalle_libro, name='libro_detalle'),
    url(r'^libros/detalle/(?P<id>\d0)/$',libros_detalle_libro, name='libro_detalle'),
    url(r'^libros/lista/$', LibroListView.as_view(), name='libro_lista'),
    url(r'^libros/crear$', LibroCreateView.as_view(), name='libro_create'),
    url(r'^libros/detalle/(?P<pk>\d+)/actualizar/$', LibroUpdateView.as_view(), name='Libro_edit'),
    url(r'^libros/detalle/(?P<pk>\d+)/eliminar/$', LibroDeleteView.as_view(), name='Libro_eliminado')


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
