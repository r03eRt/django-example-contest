# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-01 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contestApp', '0032_auto_20161101_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='url',
            field=models.ImageField(default='media/default.png', max_length=255, upload_to='treasure_images', verbose_name='Ruta'),
        ),
    ]