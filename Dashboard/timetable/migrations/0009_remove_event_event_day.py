# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 10:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0008_auto_20170322_1907'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_day',
        ),
    ]
