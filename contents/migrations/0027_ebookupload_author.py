# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-25 17:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0026_remove_ebookupload_intro'),
    ]

    operations = [
        migrations.AddField(
            model_name='ebookupload',
            name='author',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
