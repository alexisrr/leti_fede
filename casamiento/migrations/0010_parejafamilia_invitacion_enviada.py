# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-17 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casamiento', '0009_direccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='parejafamilia',
            name='invitacion_enviada',
            field=models.BooleanField(default=False),
        ),
    ]