# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-08 21:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='description',
            name='course_desc',
        ),
        migrations.AddField(
            model_name='course',
            name='description',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Description',
        ),
    ]
