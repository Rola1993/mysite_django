# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-21 22:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('canteen', '0024_auto_20180518_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='menu_type',
        ),
        migrations.AddField(
            model_name='dish',
            name='description',
            field=models.CharField(max_length=100, null='Add description for this dish'),
        ),
        migrations.RemoveField(
            model_name='canteen',
            name='manager',
        ),
        migrations.AddField(
            model_name='canteen',
            name='manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='manager', to=settings.AUTH_USER_MODEL),
        ),
    ]