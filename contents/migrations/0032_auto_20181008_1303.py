# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-08 13:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0031_auto_20181008_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='politicalforum',
            name='Articles',
        ),
        migrations.RemoveField(
            model_name='politicalforum',
            name='Polling',
        ),
        migrations.RemoveField(
            model_name='politicalforum',
            name='Survey',
        ),
    ]
