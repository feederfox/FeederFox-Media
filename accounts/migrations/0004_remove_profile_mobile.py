# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-08 16:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180808_1608'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Mobile',
        ),
    ]
