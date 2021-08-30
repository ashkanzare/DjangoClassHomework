from django import forms


from django.contrib.auth.models import User
from .models import Student, StudentCourse

from .vars import *


class RegisterStudent(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user', 'registration_confirmation']

        help_texts = {
            'phone': PHONE_HELP_TEXT,
        }

        error_messages = {
            'personal_id': {
                'unique': INVALID_PERSON_ID,
            },
        }


class RegisterUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password',)
        labels = {
            'username': USERNAME,
            'password': PASSWORD
        }
        help_texts = {
            'username': USERNAME_HELP_TEXT,
        }
        error_messages = {
            'username': {
                'unique': INVALID_USERNAME,
            }
        }


class StudentCourseForm(forms.ModelForm):
    class Meta:
        model = StudentCourse
        fields = '__all__'


class EditProfileStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class UserLogin(forms.Form):
    username = forms.CharField(max_length=1000, label=USERNAME)
    password = forms.CharField(max_length=1000, widget=forms.PasswordInput(), label=PASSWORD)
