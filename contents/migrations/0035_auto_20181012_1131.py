# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-12 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0034_newspaperadmin'),
    ]

    operations = [
        migrations.CreateModel(
            name='EbookAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Ebook_images/')),
                ('pdf', models.FileField(upload_to='Ebooks/')),
                ('author', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='politicalcommentsystem',
            name='comment_title',
        ),
        migrations.AlterField(
            model_name='newspaper',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='NewsPaper/'),
        ),
        migrations.AlterField(
            model_name='newspaperadmin',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='NewsPaperAdmin/'),
        ),
    ]
