# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-28 23:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contestApp', '0015_auto_20161027_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='votes',
        ),
        migrations.AddField(
            model_name='picture',
            name='points',
            field=models.IntegerField(default=0, verbose_name='puntos'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email del votante'),
        ),
    ]
