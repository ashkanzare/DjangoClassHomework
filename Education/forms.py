from django import forms

from django.contrib.auth.models import User
from .models import Student, StudentCourse


class RegisterStudent(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user']


class RegisterUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class StudentCourseForm(forms.ModelForm):
    class Meta:
        model = StudentCourse
        fields = '__all__'


class EditProfileStudent(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['study_field', 'personal_id', 'entry_date']


class UserLogin(forms.Form):
    username = forms.CharField(max_length=1000)
    password = forms.CharField(max_length=1000, widget=forms.PasswordInput())

