# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-29 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contestApp', '0021_auto_20161029_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='points',
            field=models.PositiveIntegerField(default=0, verbose_name='Puntos'),
        ),
    ]