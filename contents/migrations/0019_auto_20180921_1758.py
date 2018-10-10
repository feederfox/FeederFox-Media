# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-21 17:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0018_auto_20180921_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='PoliticalPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Position', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='politicalforum',
            name='Position',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contents.PoliticalPosition'),
            preserve_default=False,
        ),
    ]
