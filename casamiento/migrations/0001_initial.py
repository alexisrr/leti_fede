# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 20:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('horario_entrada', models.TimeField()),
            ],
        ),
    ]
