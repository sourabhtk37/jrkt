# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 08:41
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_col_sel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='contact',
            field=models.IntegerField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(code='Invalid number', message='Length has to be 10', regex='^\\d{10}$')]),
        ),
    ]
