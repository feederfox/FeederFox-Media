# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-31 10:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0022_auto_20180830_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='Magazines',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Publishing_House', models.CharField(max_length=100)),
                ('Magazine_Name', models.CharField(max_length=100)),
                ('Add_Thumbnail', models.FileField(upload_to='Magazine_Thumbnails/')),
                ('Add_Magazine', models.FileField(upload_to='Magazines/')),
                ('Language', models.CharField(max_length=100)),
                ('Category', models.CharField(choices=[('1', 'Entertainment'), ('2', 'Sports'), ('3', 'Health'), ('4', 'Business')], max_length=100)),
                ('Periodicity', models.CharField(choices=[('Daily', 'Daily'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly'), ('Yearly', 'Yearly')], max_length=100)),
                ('Place', models.CharField(max_length=400)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
