# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-10 09:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contents', '0033_politicalcommentsystem'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPaperAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('mainedition', models.CharField(blank=True, max_length=100, null=True)),
                ('subedition', models.CharField(blank=True, max_length=100, null=True)),
                ('Uploaded_at', models.CharField(max_length=100)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
