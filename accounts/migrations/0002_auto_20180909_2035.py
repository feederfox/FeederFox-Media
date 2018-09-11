# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-09 20:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_auto_20180909_2035'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Place',
        ),
        migrations.AddField(
            model_name='post',
            name='Main_Edition',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='State',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contents.State'),
        ),
        migrations.AddField(
            model_name='post',
            name='Sub_Edition',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='magazines',
            name='Category',
            field=models.CharField(choices=[('1', 'Entertainment'), ('2', 'Sports'), ('3', 'Health'), ('4', 'Business')], max_length=100),
        ),
        migrations.AlterField(
            model_name='magazines',
            name='Periodicity',
            field=models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Yearly', 'Yearly')], max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='Sub_Editions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contents.Sub_Edition'),
        ),
    ]
