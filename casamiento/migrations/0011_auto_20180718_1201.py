# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-18 12:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('casamiento', '0010_parejafamilia_invitacion_enviada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitado',
            name='grupo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='casamiento.Grupo'),
        ),
        migrations.AlterField(
            model_name='invitado',
            name='menu',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='casamiento.Menu'),
        ),
    ]
