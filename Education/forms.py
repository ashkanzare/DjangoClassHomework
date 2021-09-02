from django import forms


from .models import User
from .models import Student, StudentCourse

from .vars import *


class RegisterStudent(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['user', 'registration_confirmation', 'register_date', 'max_units']

        error_messages = {
            'personal_id': {
                'unique': INVALID_PERSON_ID,
            },
        }


class RegisterUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password', 'image', 'phone')
        labels = {
            'username': USERNAME,
            'password': PASSWORD,
            'phone': PHONE,
            'image': PHOTO,
        }
        help_texts = {
            'username': USERNAME_HELP_TEXT,
            'phone': PHONE_HELP_TEXT,
            'image': PHOTO_HELP_TEXT,
        }
        error_messages = {
            'username': {
                'unique': INVALID_USERNAME,
            },
            'phone': {
                'unique': INVALID_PHONE,
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
    user_type = forms.ChoiceField(
        widget=forms.Select,
        choices=USER_TYPE_CHOICES,
        label=USER_TYPE
    )
