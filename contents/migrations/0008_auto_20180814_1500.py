# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-14 15:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0007_auto_20180814_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Articles/'),
        ),
        migrations.AlterField(
            model_name='ebook',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Ebook/'),
        ),
        migrations.AlterField(
            model_name='magazine',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Magazine/'),
        ),
        migrations.AlterField(
            model_name='socialchannel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='SocialChannel/'),
        ),
    ]
