# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welfare', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='is_resolved',
            field=models.BooleanField(default=False),
        ),
    ]
