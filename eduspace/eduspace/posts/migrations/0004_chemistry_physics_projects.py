# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 08:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0003_auto_20160624_0835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chemistry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topics', models.CharField(max_length=100)),
                ('theory', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=200)),
                ('video', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Physics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topics', models.CharField(max_length=100)),
                ('theory', models.CharField(max_length=200)),
                ('details', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=200)),
                ('video', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topics', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=500)),
                ('video', models.CharField(max_length=200)),
            ],
        ),
    ]