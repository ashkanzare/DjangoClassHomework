import django.contrib.auth
from django.contrib.auth.decorators import user_passes_test

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from rest_framework import viewsets, generics

from .models import Course, StudentCourse, Student, College, Lesson, User
from .forms import RegisterStudent, StudentCourseForm, EditProfileStudent, UserLogin, RegisterUser
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib import messages
from .vars import *
from django.contrib.auth.views import LogoutView
import logging


logger = logging.getLogger('django')

# user test functions
def check_user_registered(user):
    check_user = User.objects.filter(id=user.id)
    if check_user:
        std = Student.objects.get(user=user)
        return not std.registration_confirmation
    return True


def check_user_is_boss(user):
    return user.groups.filter(name='Boss').exists()


# Create your views here.


class CourseListView(generic.ListView):
    template_name = 'Education/courses.html'
    queryset = Course.objects.all()


class StudentCourseListView(generic.ListView):
    template_name = 'Education/student/std_courses.html'

    def get_queryset(self):
        queryset = Course.objects.filter(studentcourse__student__user_id=self.request.user.id)
        return queryset


class HomeView(generic.TemplateView):
    template_name = 'Education/home.html'


class EducateInfoView(generic.TemplateView):
    template_name = 'Education/educate/info.html'


class StudentRequestsView(generic.ListView):
    template_name = 'Education/educate/stds_requests.html'
    queryset = Student.objects.filter(registration_confirmation=False)


class AllStudentsView(generic.ListView):
    template_name = 'Education/educate/students.html'
    queryset = Student.objects.all()


def detail(request, course_id):
    if request.method == 'GET':
        context = dict()
        context['course_info'] = StudentCourse.objects.filter(course=course_id)
        return render(request, 'Education/course-detail.html', context=context)


@user_passes_test(check_user_registered)
def register(request):
    form = RegisterStudent()
    user_form = RegisterUser()
    if request.method == 'POST':
        user_form = RegisterUser(request.POST)
        form = RegisterStudent(request.POST, request.FILES)
        if form.is_valid() and user_form.is_valid():
            user, created = User.objects.get_or_create(username=user_form.cleaned_data['username'])
            if created:
                user.set_password(user_form.cleaned_data['password'])
                user.save()
                std_group = Group.objects.get(name='Student')
                std_group.user_set.add(user)
                new_std = form.save(commit=False)
                new_std.user = user
                new_std.save()
                messages.success(request, REGISTER_SUCCESS)
                return render(request, 'Education/home.html')
        messages.error(request, form.errors.as_text())
        messages.error(request, user_form.errors.as_text())
        return redirect('Education:register')

    context = {
        'form': form,
        'user': user_form
    }
    return render(request, 'Education/auth/register.html', context=context)


#
# def register_course(request):
#     form = StudentCourseForm()
#     if request.method == 'POST':
#         form = StudentCourseForm(request.POST, request.FILES)
#         if StudentCourse.objects.filter(student__id=form['student'].value()):
#             return HttpResponse("This student is already have this course.")
#         elif form.is_valid():
#             form.save()
#             return HttpResponse("Course successfully submitted for student.")
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'Education/std_course.html', context=context)


def register_course(request):
    if request.method == 'GET':
        std = Student.objects.get(user=request.user)
        courses = Course.objects.filter(college=std.study_field.college)
        context = {
            'courses': courses,
            'std': std
        }
        return render(request, 'Education/student/register-course.html', context=context)


def edit(request, previous_path, std_id):
    std = get_object_or_404(Student, id=std_id)
    form = EditProfileStudent(instance=std)
    if request.method == 'POST':
        if check_user_is_boss(request.user) or previous_path == 'requests':
            form = EditProfileStudent(request.POST, request.FILES, instance=std)

            if form.is_valid():
                form.save()
                return redirect('Education:all_students')
        else:
            return HttpResponse('شما اجازه دسترسی به این بخش را ندارید')

    context = {
        'form': form,
        'std_id': std.id,
        'previous_path': request.META.get('HTTP_REFERER').split('/')[-2],
    }
    return render(request, 'Education/educate/edit.html', context=context)


def user_login(request):
    form = UserLogin()
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():

            user = authenticate(username=form.data['username'], password=form.data['password'])
            if user:
                if user.user_type == form.data['user_type']:
                    login(request, user)
                    return redirect('Education:home')
                messages.error(request, INVALID_LEVEL)
                return redirect('Education:login')
            messages.error(request, INVALID_USERNAME_PASSWORD)
            logger.info('username or password was incorrect.')
            return redirect('Education:login')
        messages.error(request, form.errors.as_text())
        return redirect('Education:login')
    context = {
        'form': form,
    }
    return render(request, 'Education/auth/login.html', context=context)
