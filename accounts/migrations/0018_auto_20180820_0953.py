# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-20 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_auto_20180819_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Application_Type',
            field=models.CharField(choices=[('1', 'Android'), ('2', 'IOS')], default='Android', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(max_length=100),
        ),
    ]
