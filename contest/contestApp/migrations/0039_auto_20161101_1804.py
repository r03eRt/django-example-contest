# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-01 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contestApp', '0038_auto_20161101_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='url',
            field=models.ImageField(blank=True, default='default.png', max_length=255, null=True, upload_to='treasure_images', verbose_name='Imagen'),
        ),
    ]