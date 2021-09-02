from rest_framework import serializers

from .models import Course, Lesson, College, Teacher


# class LessonSerializer(serializers.ModelSerializer):
#     items = serializers.RelatedField(many=True, read_only=True)
#
#     class Meta:
#         model = Lesson
#         fields = '__all__'

# class CourseSerializer(serializers.ModelSerializer):
#     lesson_name = serializers.RelatedField(source='lesson__name', read_only=True)
#
#     class Meta:
#         model = Course
#         fields = ('id', 'lesson_name')
#

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('last_name', )


class CollegeSerializer(serializers.ModelSerializer):
    class Meta:
        model = College
        fields = ('name',)


class CourseSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(required=True)
    college = CollegeSerializer(required=True)
    teacher = TeacherSerializer(required=True)

    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        """
        Overriding the default create method of the Model serializer.
        :param validated_data: data containing all the details of course
        :return: returns a successfully created course record
        """
        lesson_data = validated_data.pop('lesson')
        college_data = validated_data.pop('college')
        teacher_data = validated_data.pop('teacher')

        lesson = LessonSerializer.create(LessonSerializer(), validated_data=lesson_data)
        college = LessonSerializer.create(CollegeSerializer(), validated_data=college_data)
        teacher = LessonSerializer.create(TeacherSerializer(), validated_data=teacher_data)

        course, created = Course.objects.update_or_create(lesson=lesson, college=college,
                                                          teacher=teacher, max_stds=validated_data.pop('max_stds'))
        return course
