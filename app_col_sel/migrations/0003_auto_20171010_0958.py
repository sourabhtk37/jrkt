# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 09:58
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_col_sel', '0002_auto_20171010_0841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegedetail',
            name='applied_students',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='students', to='app_col_sel.Student'),
        ),
        migrations.AlterField(
            model_name='student',
            name='contact',
            field=models.IntegerField(unique=True, validators=[django.core.validators.RegexValidator(code='Invalid number', message='Length has to be 10', regex='^\\d{10}$')]),
        ),
    ]
