# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-16 09:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='date',
        ),
    ]
