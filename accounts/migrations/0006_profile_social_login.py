# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-09 12:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20181009_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Social_login',
            field=models.CharField(choices=[('0', 'Normal'), ('1', 'Facebook'), ('2', 'GooglePlus')], max_length=100, null=True),
        ),
    ]
