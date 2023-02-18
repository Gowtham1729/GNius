# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 08:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('terashare', '0007_auto_20170311_1500'),
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses_reg',
            name='course10',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course10', to='terashare.Course'),
        ),
        migrations.AddField(
            model_name='courses_reg',
            name='course11',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course11', to='terashare.Course'),
        ),
        migrations.AddField(
            model_name='courses_reg',
            name='course12',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course12', to='terashare.Course'),
        ),
        migrations.AddField(
            model_name='courses_reg',
            name='course2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course2', to='terashare.Course'),
        ),
        migrations.AddField(
            model_name='courses_reg',
            name='course3',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course3', to='terashare.Course'),
        ),
        migrations.AddField(
            model_name='courses_reg',
            name='course4',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course4', to='terashare.Course'),
        ),
        migrations.AddField(
            model_name='courses_reg',
            name='course5',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course5', to='terashare.Course'),
        ),
        migrations.AddField(
            model_name='courses_reg',
            name='course6',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course6', to='terashare.Course'),
        ),
        migrations.AddField(
            model_name='courses_reg',
            name='course7',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course7', to='terashare.Course'),
        ),
        migrations.AddField(
            model_name='courses_reg',
            name='course8',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course8', to='terashare.Course'),
        ),
        migrations.AddField(
            model_name='courses_reg',
            name='course9',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course9', to='terashare.Course'),
        ),
        migrations.AlterField(
            model_name='courses_reg',
            name='course1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course1', to='terashare.Course'),
        ),
    ]