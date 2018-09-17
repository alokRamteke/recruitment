# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-11 12:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0006_auto_20180911_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='difficulty',
            field=models.IntegerField(choices=[(1, 'Easy'), (2, 'Medium'), (3, 'Hard')], max_length=6),
        ),
    ]
