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
from libros.views import home_libros , lista_libros, detalle_libro
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^libros/$', home_libros, name='home_libros'),
    url(r'^libros/lista/$', lista_libros, name='lista'),
    url(r'^libros/detalle/(?P<id>\d)/$', detalle_libro, name='detalle'),
    url(r'^libros/detalle/(?P<id>\d0)/$', detalle_libro, name='detalle'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)