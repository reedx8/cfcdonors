# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-08 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_auto_20171206_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor_list',
            name='fileobj',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
