# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-18 08:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0014_remove_membership_num'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='membership',
            options={'ordering': ('my_order',)},
        ),
        migrations.AddField(
            model_name='membership',
            name='my_order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
