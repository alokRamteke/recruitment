# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-14 12:06
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0009_auto_20180912_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='contact_no',
            field=models.CharField(max_length=13, validators=[django.core.validators.RegexValidator(message='Enter correct Contact no.', regex='^\\+?1?\\d{10,13}$')]),
        ),
    ]
