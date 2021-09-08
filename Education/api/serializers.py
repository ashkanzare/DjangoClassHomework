from rest_framework import serializers

from ..models import Course, Lesson, College, Teacher, Student, User, StudyField, StudentCourse


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', ]


class StudyFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyField
        fields = '__all__'


class StudyFieldStudentSerializer(serializers.ModelSerializer):
    students = serializers.StringRelatedField(many=True)

    class Meta:
        model = StudyField
        fields = ['students']


class CollegeStudentSerializer(serializers.ModelSerializer):
    students = serializers.StringRelatedField(many=True)

    class Meta:
        model = College
        fields = ['name', 'students']


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Teacher
        fields = '__all__'


class StudentsSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Student
        fields = '__all__'


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ('name',)


class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(required=True, many=False)
    college = CollegeSerializer(required=True, many=False)
    teacher = TeacherSerializer(required=True, many=False)

    class Meta:
        model = Course
        fields = '__all__'


class SelectCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentCourse
        fields = '__all__'

