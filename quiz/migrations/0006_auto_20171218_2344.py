# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-18 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_userprofile_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.DateField(),
        ),
    ]