# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-08 11:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0030_politicalforum_polling'),
    ]

    operations = [
        migrations.AddField(
            model_name='politicalforum',
            name='Articles',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='politicalforum',
            name='Survey',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
