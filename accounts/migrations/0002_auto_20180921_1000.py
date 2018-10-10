# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-21 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='magazines',
            old_name='Place',
            new_name='State',
        ),
        migrations.AddField(
            model_name='magazines',
            name='Uploaded_at',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
