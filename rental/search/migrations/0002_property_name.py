# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-11 19:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='name',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
