import django.contrib.auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Course, StudentCourse, Student
from .forms import RegisterStudent, StudentCourseForm, EditProfileStudent, UserLogin, RegisterUser
from django.contrib.auth import authenticate

# Create your views here.

class CourseListView(generic.ListView):
    template_name = 'Education/courses.html'
    queryset = Course.objects.all()


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
                new_std = form.save(commit=False)
                new_std.user = user
                new_std.save()
                return HttpResponse("Your Registration submitted successfully")
            return HttpResponse("Username has already taken")
        return HttpResponse("Please fill forms with valid inputs")
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
            std.save()
            return HttpResponse("Profile edited successfully")

    context = {
        'form': form,
    }
    return render(request, 'Education/edit.html', context=context)


def student_login(request):
    form = UserLogin()
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            print()
            if authenticate(username=form.data['username'], password=form.data['password']):
                return HttpResponse('you are logged in')
            else:
                return HttpResponse('wrong username or password')
    context = {
        'form': form,
    }
    return render(request, 'Education/login.html', context=context)