# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 20:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('casamiento', '0006_menu'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitado',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='casamiento.Menu'),
        ),
    ]