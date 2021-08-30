import django.contrib.auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import generic
from .models import Course, StudentCourse, Student
from .forms import RegisterStudent, StudentCourseForm, EditProfileStudent, UserLogin, RegisterUser
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import Group
from django.contrib import messages
from .vars import *
from django.contrib.auth.views import LogoutView


# Create your views here.


class CourseListView(generic.ListView):
    template_name = 'Education/courses.html'
    queryset = Course.objects.all()


class HomeView(generic.TemplateView):
    template_name = 'Education/home.html'


class EducateInfoView(generic.TemplateView):
    template_name = 'Education/info.html'


class StudentRequestsView(generic.ListView):
    template_name = 'Education/stds_requests.html'
    queryset = Student.objects.filter(registration_confirmation=False)


def detail(request, course_id):
    if request.method == 'GET':
        context = dict()
        context['course_info'] = StudentCourse.objects.filter(course=course_id)
        return render(request, 'Education/course-detail.html', context=context)


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
                std_group = Group.objects.get(name='Students')
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
    return render(request, 'Education/register.html', context=context)


def register_course(request):
    form = StudentCourseForm()
    if request.method == 'POST':
        form = StudentCourseForm(request.POST, request.FILES)
        if StudentCourse.objects.filter(student__id=form['student'].value()):
            return HttpResponse("This student is already have this course.")
        elif form.is_valid():
            form.save()
            return HttpResponse("Course successfully submitted for student.")

    context = {
        'form': form,
    }
    return render(request, 'Education/std_course.html', context=context)


def edit(request, std_id):
    std = get_object_or_404(Student, id=std_id)
    form = EditProfileStudent(instance=std)
    if request.method == 'POST':
        form = EditProfileStudent(request.POST, request.FILES)
        if form.is_valid():
            std.first_name = form.data['first_name']
            std.last_name = form.data['last_name']
            std.birthday = form.data['birthday']
            std.address = form.data['address']
            std.email = form.data['email']
            std.image = form.data['image']
            std.personal_id = form.data['personal_id']
            std.registration_confirmation = form.data['registration_confirmation']
            std.study_field = form.data['study_field']

            std.save()
            return HttpResponse("Profile edited successfully")

    context = {
        'form': form,
    }
    return render(request, 'Education/edit.html', context=context)


def user_login(request):
    form = UserLogin()
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            user = authenticate(username=form.data['username'], password=form.data['password'])
            if user:
                login(request, user)
                return redirect('Education:home')
            messages.error(request, INVALID_USERNAME_PASSWORD)
            return redirect('Education:login')
        messages.error(request, form.errors.as_text())
        return redirect('Education:login')
    context = {
        'form': form,
    }
    return render(request, 'Education/login.html', context=context)

