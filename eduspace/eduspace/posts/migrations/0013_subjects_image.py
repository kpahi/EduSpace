# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_remove_explain_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjects',
            name='image',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
    ]
