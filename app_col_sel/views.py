# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .forms import SearchCollege, StudentForm
from .models import CollegeDetail, Student


def home(request):
    
    if request.method == 'GET':
        form = SearchCollege()
        return render(request, 'homepage.html', {'form':form})


def col_list(request):

    if request.method == 'POST':
        form = SearchCollege(request.POST)

        if form.is_valid():

            col_listing = CollegeDetail.objects.filter(city=form.cleaned_data['city'],
                                                    course=form.cleaned_data['course'],
                                                    level=form.cleaned_data['level']).order_by('fees', '-avg_salary')

            return render(request, 'col_list.html', {'col_listing':col_listing})

        else:
            return HttpResponse("form invalid")


def col_submit(request, col_id):

    if request.method == 'GET':
        college = CollegeDetail.objects.get(id=col_id)
        form = StudentForm()

        return render(request, 'college.html', {'college':college, 'form':form})

    if request.method == 'POST':
        form = StudentForm(request.POST)
        print(form.is_valid())

        if form.is_valid():
            student = Student.objects.create(name=form.cleaned_data['name'],
                                             address=form.cleaned_data['address'],
                                             contact=form.cleaned_data['contact'],
                                             dob=form.cleaned_data['dob'],
                                             gender=form.cleaned_data['gender'])

            college = CollegeDetail.objects.update(applied_students=student)
            
            return HttpResponse('Success')
