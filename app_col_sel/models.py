# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import RegexValidator


class CollegeDetail(models.Model):
    """docstring for College"""
    
    LEVEL_CHOICES = (
        (1, 'GRAD'),
        (2, 'POSTGRAD'),
    )

    name = models.CharField(max_length=200)
    fees = models.IntegerField()
    avg_salary = models.IntegerField()
    level = models.IntegerField(choices=LEVEL_CHOICES)

    city = models.CharField(max_length=100)
    course = models.CharField(max_length=200)
    applied_students = models.ForeignKey('Student', 
                                         related_name='college_applied', 
                                         null=True,
                                         blank=True)

    def __unicode__(self):
        return str(self.name) 


class Student(models.Model):
    """docstring for Student"""
    
    GENDER_CHOICES = (
        (1, 'MALE'),
        (2, 'FEMALE'),
        (3, 'OTHER')
    )

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=1000)
    contact = models.IntegerField(unique=True, 
                                  validators=[RegexValidator(regex='^\d{10}$', message='Length has to be 10', code='Invalid number')])
    dob = models.DateField(max_length=8)
    gender = models.IntegerField(choices=GENDER_CHOICES)

    def __unicode__(self):
        return str(self.name) 