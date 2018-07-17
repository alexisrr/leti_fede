# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *


class GrupoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Grupo._meta.fields]


class InvitadoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Invitado._meta.fields]
    list_display.append('url_invitacion')
    list_filter = ['invitacion_enviada', 'confirmado', 'grupo', 'menu']
    search_fields = ['nombre', 'apellido']


class ParejaFamiliaAdmin(admin.ModelAdmin):
    list_display = ['nombre_pareja_familia', 'get_invitados', 'url_invitacion', 'invitacion_enviada']
    search_fields = ['invitado__nombre', 'invitado__apellido']


class MenuAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Menu._meta.fields]


class MenuOtroAdmin(admin.ModelAdmin):
    list_display = [f.name for f in MenuOtro._meta.fields]
    search_fields = ['invitado']


class DireccionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Direccion._meta.fields]


admin.site.register(Grupo, GrupoAdmin)
admin.site.register(Invitado, InvitadoAdmin)
admin.site.register(ParejaFamilia, ParejaFamiliaAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuOtro, MenuOtroAdmin)
admin.site.register(Direccion, DireccionAdmin)