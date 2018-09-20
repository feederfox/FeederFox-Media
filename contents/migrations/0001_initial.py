# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-14 17:35
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=10000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='Articles/')),
            ],
        ),
        migrations.CreateModel(
            name='Dummy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.URLField(max_length=100)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Ebook',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='Ebooks/')),
            ],
        ),
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='Magazine/')),
                ('language', models.CharField(max_length=100, null=True)),
                ('category', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Main_Edition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NationalNewsChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='NationalNewsPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='NewsPaper',
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
        migrations.CreateModel(
            name='PoliticalForum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='Politicians/')),
                ('Synopsis', models.CharField(max_length=10000)),
                ('Projects_Taken', models.CharField(blank=True, max_length=10000, null=True)),
                ('Educational_Qualification', models.CharField(max_length=100)),
                ('Family_History', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='PublisherDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Language', models.CharField(max_length=100)),
                ('Add_Logo', models.FileField(blank=True, null=True, upload_to='publisher_details/')),
                ('Type', models.CharField(choices=[('1', 'Paper'), ('2', 'Magazine')], max_length=100)),
                ('Main_Edition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contents.Main_Edition')),
            ],
        ),
        migrations.CreateModel(
            name='RegionalNewsChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='RegionalNewsPaper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='SocialChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='SocialChannel/')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='States/')),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Edition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Edition', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='publisherdetail',
            name='State',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.State'),
        ),
        migrations.AddField(
            model_name='publisherdetail',
            name='Sub_Edition',
            field=models.ManyToManyField(blank=True, null=True, to='contents.Edition'),
        ),
        migrations.AddField(
            model_name='publisherdetail',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='main_edition',
            name='State',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.State'),
        ),
        migrations.AddField(
            model_name='edition',
            name='State',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contents.State'),
        ),
    ]
