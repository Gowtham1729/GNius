# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-22 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terashare', '0019_file_reports'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='reports',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]