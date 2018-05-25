# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-16 00:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0022_auto_20180511_0106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='conversation',
            old_name='street_address',
            new_name='name_address',
        ),
        migrations.RemoveField(
            model_name='conversation',
            name='State',
        ),
        migrations.RemoveField(
            model_name='conversation',
            name='city',
        ),
        migrations.AlterField(
            model_name='menu',
            name='dishtype_list',
            field=models.CharField(default='["food","drinks"]', max_length=200),
        ),
    ]