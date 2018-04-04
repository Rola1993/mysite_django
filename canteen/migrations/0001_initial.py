# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-06 01:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Canteen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('nums_stars', models.IntegerField()),
            ],
            options={
                'ordering': ['-nums_stars'],
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=30)),
                ('nums_stars', models.IntegerField()),
                ('resturant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canteen.Canteen')),
            ],
        ),
    ]
