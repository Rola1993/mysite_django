# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-18 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0023_auto_20180516_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='dish_type',
            field=models.CharField(default='food', max_length=20),
        ),
    ]
