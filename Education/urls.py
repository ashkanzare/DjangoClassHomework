from django.urls import path
from .views import CourseListView, detail, register, register_course

app_name = 'Education'

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='courses'),
    path('course-detail/<int:course_id>', detail, name='detail'),
    path('register/', register, name='register'),
    path('register-course/', register_course, name='register_course'),
]
