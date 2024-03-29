# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-20 16:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('terashare', '0008_coursetimings_days'),
        ('profiles', '0006_userprofile_course_reg'),
        ('timetable', '0002_auto_20170320_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursesReg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course1', to='terashare.Course')),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='profiles.UserProfile')),
            ],
        ),
        migrations.RemoveField(
            model_name='courses_reg',
            name='course1',
        ),
        migrations.RemoveField(
            model_name='courses_reg',
            name='course10',
        ),
        migrations.RemoveField(
            model_name='courses_reg',
            name='course11',
        ),
        migrations.RemoveField(
            model_name='courses_reg',
            name='course12',
        ),
        migrations.RemoveField(
            model_name='courses_reg',
            name='course2',
        ),
        migrations.RemoveField(
            model_name='courses_reg',
            name='course3',
        ),
        migrations.RemoveField(
            model_name='courses_reg',
            name='course4',
        ),
        migrations.RemoveField(
            model_name='courses_reg',
            name='course5',
        ),
        migrations.RemoveField(
            model_name='courses_reg',
            name='course6',
        ),
        migrations.RemoveField(
            model_name='courses_reg',
            name='course7',
        ),
        migrations.RemoveField(
            model_name='courses_reg',
            name='course8',
        ),
        migrations.RemoveField(
            model_name='courses_reg',
            name='course9',
        ),
        migrations.RemoveField(
            model_name='courses_reg',
            name='user_profile',
        ),
        migrations.DeleteModel(
            name='Courses_Reg',
        ),
    ]
