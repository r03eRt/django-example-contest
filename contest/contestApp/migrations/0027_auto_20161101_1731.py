# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-01 17:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contestApp', '0026_auto_20161101_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Fecha creacion'),
        ),
    ]
