from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import Course, StudentCourse, Student
from .forms import RegisterStudent, StudentCourseForm


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
    if request.method == 'POST':
        form = RegisterStudent(request.POST, request.FILES)
        if Student.objects.filter(personal_id=form['personal_id'].value()):
            return HttpResponse("This student is already in database")
        elif form.is_valid():
            form.save()
            return HttpResponse("Your Registration submitted successfully")

    context = {
        'form': form
    }
    return render(request, 'Education/register.html', context=context)


def register_course(request):
    form = StudentCourseForm()
    if request.method == 'POST':
        form = StudentCourseForm(request.POST)
        if StudentCourse.objects.filter(student__id=form['student'].value()):
            return HttpResponse("This student is already have this course.")
        elif form.is_valid():
            form.save()
            return HttpResponse("Course successfully submitted for student.")

    context = {
        'form': form
    }
    return render(request, 'Education/std_course.html', context=context)

