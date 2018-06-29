# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


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
    grupo = models.ForeignKey(Grupo, null=True)
    menu = models.ForeignKey(Menu, null=True)

    def __unicode__(self):
        return '{}, {}'.format(self.nombre, self.apellido)


class ParejaFamilia(models.Model):
    nombre_pareja_familia = models.CharField(max_length=255)
    invitado = models.ManyToManyField(Invitado)

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



