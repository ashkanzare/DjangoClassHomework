from django.urls import path, include
from Education.api.views import CourseViewSet, StudentsViewSet, TeacherViewSet, StudyDetailViewSet, \
    StudyFieldStudentViewSet, SelectCourseView, CheckCourseView, CollegeStudentViewSet, SelectCourseViewSet
from rest_framework import routers

app_name = 'education_api'

router = routers.DefaultRouter()
router.register('', SelectCourseViewSet, basename='StudentCourse')

urlpatterns = [
    path('', include(router.urls)),
    path('courses-api/<str:text>', CourseViewSet.as_view(), name='courses-api'),
    path('students/', StudentsViewSet.as_view(), name='students-api'),
    path('teachers/', TeacherViewSet.as_view(), name='teachers-api'),
    path('studyfield-detail/<int:study_id>', StudyDetailViewSet.as_view(), name='study-detail'),
    path('study-fields/', StudyFieldStudentViewSet.as_view(), name='study_fields'),
    path('college-students/', CollegeStudentViewSet.as_view(), name='college_students'),
    path('select-course/', SelectCourseView.as_view(), name='select_course'),
    path('check-courses/', CheckCourseView.as_view(), name='check_courses'),
]
