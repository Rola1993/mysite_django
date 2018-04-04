# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-03-19 20:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('canteen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('info', models.CharField(max_length=200)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='dish',
            options={'ordering': ['-nums_stars']},
        ),
        migrations.AddField(
            model_name='canteen',
            name='manager',
            field=models.ManyToManyField(related_name='manager', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='canteen',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='dish',
            name='resturant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Dish', to='canteen.Menu'),
        ),
        migrations.AddField(
            model_name='menu',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Menu', to='canteen.Canteen'),
        ),
    ]