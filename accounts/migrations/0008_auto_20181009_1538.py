# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-09 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20181009_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Firstname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='Lastname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
