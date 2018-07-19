"""leti URL Configuration

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

from casamiento.views import importar_invitados_csv, invitar_pareja_familia, confirmar_invitado, invitar_individual
from casamiento.views import guardar_confirmacion, principal, generate_database

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^database_gen/$', generate_database),
    url(r'^importar/invitados/$', importar_invitados_csv),
    url(r'^invitacion/pareja-familia/(?P<id_pareja_familia>\d+)/$', invitar_pareja_familia),
    url(r'^invitacion/(?P<id_invitado>\d+)/$', invitar_individual),
    url(r'^confirmar-invitado/(?P<id_invitado>\d+)/$', confirmar_invitado, name="confirmar_invitado"),
    url(r'^guardar-confirmacion/(?P<id_invitado>\d+)/$', guardar_confirmacion, name="guardar_confirmacion"),
    url(r'^$', principal, name="principal"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
