# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-03 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewsFeeds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsfeed',
            name='category',
            field=models.CharField(choices=[('1', 'Headlines/Breaking News'), ('2', 'Education'), ('3', 'Entertainment'), ('4', 'Business'), ('5', 'Sports'), ('6', 'LifeStyle'), ('7', 'Social'), ('8', 'World/International'), ('9', 'Global')], max_length=100),
        ),
    ]
