# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-04-03 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0014_auto_20180403_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='last_message',
            field=models.CharField(max_length=30, null=True),
        ),
    ]