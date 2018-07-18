# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import base64


class Grupo(models.Model):
    nombre = models.CharField(max_length=255)
    horario_entrada = models.TimeField()

    def __unicode__(self):
        return '{}, {}'.format(self.nombre, self.horario_entrada)


class Menu(models.Model):
    nombre = models.CharField(max_length=255)

    def __unicode__(self):
        return self.nombre


class Invitado(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    invitacion_enviada = models.BooleanField(default=False)
    confirmado = models.BooleanField(default=False)
    confirmado_el = models.DateTimeField(null=True, blank=True)
    grupo = models.ForeignKey(Grupo, null=True, blank=True)
    menu = models.ForeignKey(Menu, null=True, blank=True)

    def url_invitacion(self):
        pf = ParejaFamilia.objects.filter(invitado=self.id).first()

        if pf is not None:
            return 'En pareja/Familia'
        else:
            return '<a href="http://fedeyleti.com.ar/invitacion/{}/?id={}">Invitacion {}</a>'\
                .format(self.id, base64.b64encode(str(self.id)),  self.nombre)

    def url_invitacion_clean(self):
        return "http://fedeyleti.com.ar/invitacion/{}/?id={}".format(self.id, base64.b64encode(str(self.id)),  self.nombre)


    url_invitacion.allow_tags = True

    def __unicode__(self):
        return '{}, {}'.format(self.nombre, self.apellido)


class ParejaFamilia(models.Model):
    nombre_pareja_familia = models.CharField(max_length=255)
    invitacion_enviada = models.BooleanField(default=False)
    invitado = models.ManyToManyField(Invitado)

    def get_invitados(self):
        return ", ".join(['{} - {}'.format(p.apellido.upper(), p.nombre) for p in self.invitado.all()])

    def url_invitacion(self):
        return '<a href="http://fedeyleti.com.ar/invitacion/pareja-familia/{}/?id={}">Invitacion {}</a>'\
            .format(self.id, base64.b64encode(str(self.id)), self.get_invitados())

    def url_invitacion_clean(self):
        return "http://fedeyleti.com.ar/invitacion/pareja-familia/{}/?id={}".format(self.id, base64.b64encode(str(self.id)), self.get_invitados())

    url_invitacion.allow_tags = True

    def __unicode__(self):
        return '{}'.format(self.nombre_pareja_familia)


class MenuOtro(models.Model):
    invitado = models.ForeignKey(Invitado)
    descripcion = models.TextField()

    def __unicode__(self):
        return '{},{}'.format(self.invitado.nombre, self.descripcion)


class Direccion(models.Model):
    nombre = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    latitud = models.FloatField()
    longitud = models.FloatField()
    link = models.TextField(null=True)
