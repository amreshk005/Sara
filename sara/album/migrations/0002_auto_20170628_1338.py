# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-28 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.CharField(default=' ', max_length=100),
        ),
        migrations.AlterField(
            model_name='album',
            name='details',
            field=models.TextField(default=' ', max_length=200),
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(default=' ', max_length=30),
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
