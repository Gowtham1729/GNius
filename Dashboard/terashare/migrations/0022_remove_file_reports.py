# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 11:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terashare', '0021_auto_20170322_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='reports',
        ),
    ]
