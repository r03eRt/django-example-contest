# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-29 11:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contestApp', '0022_auto_20161029_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='picture',
            name='points',
        ),
    ]