# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-18 23:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_remove_userprofile_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='date_joined',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
