# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-13 17:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_auto_20180513_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownerinfo',
            name='propertie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='search.Property'),
        ),
    ]
