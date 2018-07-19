# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from leti.settings import BASE_DIR
import os

from casamiento.models import Invitado, Grupo, ParejaFamilia, Menu, MenuOtro
import base64
import datetime


def importar_invitados_csv(request):
    data_file = os.path.join(BASE_DIR, 'data/lista_invitados.csv')

    with open(data_file, 'r') as im:
        im = im.readlines()
        for x, line in enumerate(im):
            line = line.decode('latin1')
            data = line.split(';')

            apellido = data[0]
            nombre = data[1]
            grupo_csv = int(data[2].strip('\r\n'))

            grupo = None

            if grupo_csv == 1:
                grupo = Grupo.objects.filter(nombre='Normal').first()

            if grupo_csv == 2:
                grupo = Grupo.objects.filter(nombre='Fiesta').first()

            invitado = Invitado(
                nombre=nombre,
                apellido=apellido,
                invitacion_enviada=False,
                confirmado=False,
                confirmado_el=None,
                grupo=grupo,
                menu=None
            )

            invitado.save()


def invitar_pareja_familia(request, id_pareja_familia):
    decoded = base64.b64decode(str(request.GET.get('id')))
    pareja_familia = None
    d_name = None

    invitado_confirmado = request.GET.get('invitado_confirmado')
    invitado_confirmado_obj = None

    if invitado_confirmado is not None:
        invitado_confirmado_obj = Invitado.objects.get(pk=invitado_confirmado)

    if int(decoded) == int(id_pareja_familia):
        pareja_familia = ParejaFamilia.objects.get(pk=id_pareja_familia)
        pareja_familia.invitados = pareja_familia.invitado.all()

        for invitado in pareja_familia.invitados:
            grupo = Grupo.objects.filter(pk=invitado.grupo_id)
            pareja_familia.grupo = grupo

        if len(pareja_familia.invitados) == 2:
            d_name = " y ".join(['{}'.format(p.nombre) for p in pareja_familia.invitados])

        if len(pareja_familia.invitados) > 2:
            d_name = ", ".join(['{}'.format(p.nombre) for p in pareja_familia.invitados])

    context = {
        'pareja': pareja_familia,
        'd_name': d_name,
        'id': id_pareja_familia,
        'invitado_confirmado_obj': invitado_confirmado_obj
    }

    return render(request, 'casamiento/invitar_pareja_familia.html', context)


def invitar_individual(request, id_invitado):
    decoded = base64.b64decode(str(request.GET.get('id')))
    invitado = None

    invitado_confirmado = request.GET.get('invitado_confirmado')
    invitado_confirmado_obj = None

    if invitado_confirmado is not None:
        invitado_confirmado_obj = Invitado.objects.get(pk=invitado_confirmado)

    if int(decoded) == int(id_invitado):
        invitado = Invitado.objects.get(pk=id_invitado)

    context = {
        'invitado': invitado,
        'd_name': invitado.nombre,
        'id': id_invitado,
        'invitado_confirmado_obj': invitado_confirmado_obj
    }

    return render(request, 'casamiento/invitar_pareja_familia.html', context)


def confirmar_invitado(request, id_invitado):
    invitado = Invitado.objects.get(pk=id_invitado)
    menus = Menu.objects.all()

    context = {
        'menus': menus,
        'invitado': invitado,
    }

    return render(request, 'casamiento/confirmar.html', context)


def guardar_confirmacion(request, id_invitado):
    invitado = Invitado.objects.get(pk=id_invitado)
    id_menu = request.POST.get('menu_id')
    menu_otro = request.POST.get('otro')

    menu = Menu.objects.get(pk=id_menu)

    try:
        if len(menu_otro)> 0:
            mo = MenuOtro(invitado=invitado, descripcion=menu_otro)
            mo.save()
    except:
        pass

    invitado.menu = menu
    invitado.confirmado = True
    invitado.confirmado_el = datetime.datetime.now()
    invitado.save()

    in_pareja = ParejaFamilia.objects.filter(invitado=invitado).first()

    if in_pareja is not None:
        redirect_url = '{}&invitado_confirmado={}'.format(in_pareja.url_invitacion_clean(), id_invitado)
        return redirect(redirect_url)

    if in_pareja is None:
        redirect_url = '{}&invitado_confirmado={}'.format(invitado.url_invitacion_clean(), id_invitado)
        return redirect(redirect_url)


def principal(request):
    return render(request, 'casamiento/principal.html')