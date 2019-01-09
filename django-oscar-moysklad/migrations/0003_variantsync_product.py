# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-01 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0013_auto_20170821_1548'),
        ('synchronizer', '0002_auto_20181101_0601'),
    ]

    operations = [
        migrations.AddField(
            model_name='variantsync',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogue.Product'),
        ),
    ]
