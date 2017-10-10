from django import forms
from django.forms.widgets import DateInput

from .models import CollegeDetail, Student


class SearchCollege(forms.Form):
    """docstring for SearchCollege"""

    LEVEL_CHOICES = (
        (1, 'GRAD'),
        (2, 'POSTGRAD'),
    )

    city = forms.CharField(max_length=100)
    course = forms.CharField(max_length=200)
    level = forms.IntegerField(widget=forms.Select(choices=LEVEL_CHOICES))

class StudentForm(forms.ModelForm):
    """docstring for CollegeSubmission"""

    class Meta:
        model = Student
        fields = ['name', 'address', 'contact', 'dob', 'gender']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'contact': forms.NumberInput,
        }
