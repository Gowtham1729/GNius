# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-08 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terashare', '0003_remove_file_stream'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='Stream',
            field=models.CharField(max_length=150, null=True),
        ),
    ]