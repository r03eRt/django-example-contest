# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-29 08:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contestApp', '0016_auto_20161028_2319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='points',
        ),
    ]