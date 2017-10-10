# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 08:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CollegeDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('fees', models.IntegerField()),
                ('avg_salary', models.IntegerField()),
                ('level', models.IntegerField(choices=[(1, 'GRAD'), (2, 'POSTGRAD')])),
                ('city', models.CharField(max_length=100, unique=True)),
                ('course', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=1000)),
                ('contact', models.IntegerField(max_length=10)),
                ('dob', models.DateField(max_length=8)),
                ('gender', models.IntegerField(choices=[(1, 'MALE'), (2, 'FEMALE')])),
            ],
        ),
        migrations.AddField(
            model_name='collegedetail',
            name='applied_students',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='students', to='app_col_sel.Student'),
        ),
    ]
