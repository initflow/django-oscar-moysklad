# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-15 11:51
from __future__ import unicode_literals

from django.db import migrations, models

from models import SyncTaskObject


def default_task_values(apps, schema_editor):
    SyncTaskObject(name='product_update_task').save()
    SyncTaskObject(name='discount_update_task').save()


class Migration(migrations.Migration):
    dependencies = [
        ('synchronizer', '0003_variantsync_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='SyncTaskObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('last_run_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.RunPython(default_task_values)
    ]
