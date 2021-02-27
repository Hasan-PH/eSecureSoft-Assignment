from decimal import Decimal
from django import forms
from .models import Student, School, Teacher, Subject

class TestForm(forms.Form):
    CHOICES = (
        ('', '----'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    name = forms.CharField(label='Name *', widget=forms.TextInput(attrs={'label': "Student Name", 'class': 'form-control',
                                                             'placeholder': "Enter Student Name"}))

    gender = forms.ChoiceField(label="Gender", choices=CHOICES, required=False,
                                     widget=forms.Select(attrs={'class': 'regDropDown'}))

    age = forms.IntegerField(widget=forms.TextInput(attrs={'type':'number', 'label': "Age", 'class': 'form-control',
                                                         'placeholder': "Enter age"}), required=False)

    birth_date = forms.DateField(label='Date of Birth *', widget=forms.SelectDateWidget(years=range(1980, 2021)))

    location = forms.CharField(widget=forms.TextInput(attrs={'label': "Location", 'class': 'form-control',
                                                         'placeholder': "Enter Location"}), required=False)

    school = forms.ModelChoiceField(label="School name *", queryset=School.objects.only("name"),
                                     widget=forms.Select(attrs={'class': 'regDropDown'}))

    teacher = forms.ModelChoiceField(label="Teacher name *", queryset=Teacher.objects.none(),
                                     widget=forms.Select(attrs={'class': 'regDropDown'}))

    subject1 = forms.ModelChoiceField(label="Subject 1 *", queryset=Subject.objects.only("name"),
                                     widget=forms.Select(attrs={'class': 'regDropDown'}))

    # subject2 = forms.ModelChoiceField(label="Subject 2", queryset=Subject.objects.only("name"),
    #                                  widget=forms.Select(attrs={'class': 'regDropDown'}), required=False)
    #
    # subject3 = forms.ModelChoiceField(label="Subject 3", queryset=Subject.objects.only("name"),
    #                                  widget=forms.Select(attrs={'class': 'regDropDown'}), required=False)

