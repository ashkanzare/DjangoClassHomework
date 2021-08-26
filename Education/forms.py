from django import forms

from .models import Student, StudentCourse


class RegisterStudent(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentCourseForm(forms.ModelForm):
    class Meta:
        model = StudentCourse
        fields = '__all__'
