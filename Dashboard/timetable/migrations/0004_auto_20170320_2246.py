# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 17:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('terashare', '0008_coursetimings_days'),
        ('timetable', '0003_auto_20170320_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesreg',
            name='course2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course2', to='terashare.Course'),
        ),
        migrations.AlterField(
            model_name='coursesreg',
            name='course1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course1', to='terashare.Course'),
        ),
    ]
