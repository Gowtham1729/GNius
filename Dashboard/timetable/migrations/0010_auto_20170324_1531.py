# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 10:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0009_remove_event_event_day'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursesreg',
            name='course11',
        ),
        migrations.RemoveField(
            model_name='coursesreg',
            name='course12',
        ),
    ]
