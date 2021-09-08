from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Course, Student, Teacher, StudentCourse, StudyField, College
from .serializers import CourseSerializer, StudentsSerializer, TeacherSerializer, \
    StudyFieldSerializer, StudyFieldStudentSerializer, SelectCourseSerializer, CollegeStudentSerializer


# user test functions

class CourseViewSet(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        text = self.kwargs['text']
        queryset = Course.objects.select_related('lesson').filter(lesson__name__contains=text)
        return queryset


class StudentsViewSet(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentsSerializer


class StudyDetailViewSet(generics.ListAPIView):
    serializer_class = StudyFieldSerializer

    def get_queryset(self):
        study_id = self.kwargs['study_id']
        queryset = StudyField.objects.filter(pk=study_id)
        print('yes')
        return queryset


class TeacherViewSet(generics.ListAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudyFieldStudentViewSet(APIView):
    def get(self, request, format=None):
        queryset = StudyField.objects.all()
        response = dict()
        response['study_fields'] = StudyFieldStudentSerializer(queryset, context={'request': request}, many=True).data
        return Response(response)


class CollegeStudentViewSet(APIView):
    def get(self, request, format=None):
        queryset = College.objects.all()
        response = dict()
        response['colleges'] = CollegeStudentSerializer(queryset, context={'request': request}, many=True).data
        return Response(response)

#
# class CollegeStudyViewSet(APIView):
#     def get(self, request, format=None):
#         queryset = College.objects.all()
#         response = dict()
#         response['colleges'] = CollegeStudyFieldSerializer(queryset, context={'request': request}, many=True).data
#         return Response(response)


class SelectCourseView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = StudentCourse.objects.all()
    serializer_class = SelectCourseSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CheckCourseView(APIView):
    def get(self, request, format=None):
        print(request.data)
        return Response([{}])

    def post(self, request, format=None):
        courses_id = dict(request.data)
        del courses_id['csrfmiddlewaretoken']
        print(courses_id)
        courses_id = {i: int(courses_id[i][0]) for i in courses_id}
        for course_id in courses_id:
            for other_course in courses_id:
                if course_id != other_course:
                    course_1 = Course.objects.get(pk=courses_id[course_id])
                    course_2 = Course.objects.get(pk=courses_id[other_course])
                    if not course_1.check_for_conflict(course_2):
                        return Response([{'status': 'conflict',
                                          'courses': {
                                              'course_1': course_1.id,
                                              'course_2': course_2.id}}])
        return Response([{'status': 'ok'}])
