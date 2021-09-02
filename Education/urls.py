from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from .views import (
    CourseListView, detail, register, register_course,
    edit, user_login, HomeView, EducateInfoView,
    StudentRequestsView, AllStudentsView, CourseViewSet
    )

app_name = 'Education'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('courses/', CourseListView.as_view(), name='courses'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('Education:login')), name='logout'),
    path('requests/', StudentRequestsView.as_view(), name='std_requests'),
    path('students/', AllStudentsView.as_view(), name='all_students'),
    path('educate-info/', EducateInfoView.as_view(), name='info'),
    path('course-detail/<int:course_id>', detail, name='detail'),
    path('register/', register, name='register'),
    path('edit/<str:previous_path>/<int:std_id>', edit, name='edit'),
    path('register-course/', register_course, name='register_course'),
    path('login/', user_login, name="login"),
    path('courses-api/<str:text>', CourseViewSet.as_view(), name='courses-api')
]
