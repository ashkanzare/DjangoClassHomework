import django.utils.timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from .vars import *


# Create your models here.

class User(AbstractUser):
    phone_regex = RegexValidator(regex=r'^9\d{9}$',
                                 message="شماره تماس باید با فرمت ۹۱۲۷۸۹۳۴۵۶ وارد شود")
    phone = models.CharField(validators=[phone_regex], max_length=10, unique=True)
    image = models.ImageField(upload_to='user_image', blank=True, null=True)

    user_type = models.CharField(max_length=500, choices=USER_TYPE_CHOICES, default=None, null=True)

    EMAIL_FIELD = 'phone'
    REQUIRED_FIELDS = ['phone']


class College(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return f"{self.name}"


class StudyField(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='study_fields')
    name = models.CharField(max_length=300, verbose_name=STUDY_FIELD)

    def __str__(self):
        return f"{self.college.name} -- {self.name}"


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name=USERNAME)
    first_name = models.CharField(max_length=200, verbose_name=FIRST_NAME)
    last_name = models.CharField(max_length=200, verbose_name=LAST_NAME)
    birthday = models.DateField(verbose_name=BIRTHDAY)
    address = models.TextField(verbose_name=ADDRESS)
    personal_id = models.CharField(max_length=200, unique=True, blank=True, null=True, verbose_name=PERSONAL_ID)
    email = models.EmailField(verbose_name=EMAIL)
    entry_date = models.DateField(null=True, blank=True, default=django.utils.timezone.now, verbose_name=ENTRY_DATE)
    register_date = models.DateField(null=True, blank=True, default=django.utils.timezone.now,
                                     verbose_name=REGISTER_DATE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(Person):
    expertise = models.CharField(max_length=200, null=True, blank=True)
    post = models.CharField(default=None, unique=True, max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Teacher: {self.first_name} {self.last_name} -- {self.expertise}"


class Staff(Person):
    expertise = models.CharField(max_length=200, null=True, blank=True)
    post = models.CharField(default=None, unique=True, max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Staff: {self.first_name} {self.last_name} -- {self.post}"


class Student(Person):
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='students', null=True)
    study_field = models.ForeignKey(StudyField, on_delete=models.CASCADE, null=True, blank=True,
                                    verbose_name=STUDY_FIELD, related_name='students')
    registration_confirmation = models.BooleanField(default=False, verbose_name=REGISTER_CONFIRM)
    max_units = models.PositiveIntegerField(default=24, verbose_name=MAX_UNITS)

    class Meta:
        permissions = [('can_write_blog', 'Can Write Blog')]

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name} -- {self.study_field} -- {self.registration_confirmation}"


class Lesson(models.Model):
    name = models.CharField(max_length=250, unique=True)
    unit = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} -- {self.unit}"


class Course(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.RESTRICT)
    teacher = models.ForeignKey(Teacher, on_delete=models.RESTRICT)
    hours = models.DecimalField(max_digits=10, decimal_places=2)
    max_stds = models.PositiveIntegerField()
    start_date = models.DateField()
    ACTIVE = True
    ENDED = False
    status = (
        (ACTIVE, 'Active'),
        (ENDED, 'Ended'),
    )
    course_status = models.BooleanField(default=ACTIVE, choices=status)

    days = (
        (SATURDAY[0], SATURDAY[1]),
        (SUNDAY[0], SUNDAY[1]),
        (MONDAY[0], MONDAY[1]),
        (THURSDAY[0], THURSDAY[1]),
        (WEDNESDAY[0], WEDNESDAY[1]),
        (TUESDAY[0], TUESDAY[1])
    )
    session_1 = models.CharField(max_length=100, choices=days, null=True, blank=True)
    session_2 = models.CharField(max_length=100, choices=days, null=True, blank=True)

    session_start_time = models.TimeField(default=django.utils.timezone.now)
    session_end_time = models.TimeField(default=django.utils.timezone.now)

    def __str__(self):
        return f"course: {self.lesson.name} -- teacher: {self.teacher.last_name} -- time: {self.session_start_time} to {self.session_end_time} in {self.session_1} and {self.session_2} "

    def check_for_conflict(self, other):
        if self.session_1 == other.session_1 or self.session_1 == other.session_2 or self.session_2 == other.session_1 or self.session_2 == other.session_2:
            if self.session_start_time == other.session_start_time:
                return False
            elif self.session_start_time < other.session_start_time < self.session_end_time:
                return False
            elif other.session_start_time < self.session_start_time < other.session_end_time:
                return False
            else:
                return True
        return True


class AllowedField(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    study_field = models.ForeignKey(StudyField, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course.lesson.name} -- {self.study_field.name}"


class StudentCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.RESTRICT, default=None)
    student = models.ForeignKey(Student, on_delete=models.RESTRICT, default=None)
    score = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"course: {self.course.lesson.name} -- student: {self.student.last_name}"
