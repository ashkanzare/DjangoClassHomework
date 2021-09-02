from django.contrib import admin
from .models import College, Student, Teacher, Course, Lesson, StudentCourse, Staff, StudyField, AllowedField, User

# Register your models here.

admin.site.register(Staff)
admin.site.register(College)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(StudentCourse)
admin.site.register(StudyField)
admin.site.register(AllowedField)
admin.site.register(User)

class CourseInline(admin.StackedInline):
    model = Course
    max_num = 3


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    inlines = [CourseInline, ]


def change_status(modeladmin, request, queryset):
    queryset.update(course_status=False)


change_status.short_description = 'تعطیل کردن کلاس ها'


class CourseAdmin(admin.ModelAdmin):
    list_display = ['lesson', 'teacher', 'course_status']
    actions = [change_status, ]


admin.site.register(Course, CourseAdmin)
