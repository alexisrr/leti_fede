# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 20:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('casamiento', '0004_auto_20180628_2046'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitado',
            name='grupo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='casamiento.Grupo'),
        ),
    ]
