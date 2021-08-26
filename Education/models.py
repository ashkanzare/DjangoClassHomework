from django.db import models


# Create your models here.
class College(models.Model):
    name = models.CharField(max_length=200)
    address = models.TextField()

    def __str__(self):
        return f"{self.name}"


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birthday = models.DateField()
    address = models.TextField()
    personal_id = models.PositiveIntegerField(unique=True, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(blank=True, null=True, max_length=200)
    image = models.ImageField(upload_to='users_images', blank=True, null=True)
    entry_date = models.DateField()
    study_field = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(Person):
    expertise = models.TextField(null=True, blank=True)
    post = models.CharField(default=None, unique=True, max_length=200, blank=True, null=True)

    def __str__(self):
        return f"Teacher: {self.first_name} {self.last_name} -- {self.study_field}"


class Student(Person):

    def __str__(self):
        return f"Student: {self.first_name} {self.last_name} -- {self.study_field}"


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

    def __str__(self):
        return f"course: {self.lesson.name} -- teacher: {self.teacher.last_name}"


class StudentCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.RESTRICT, default=None)
    student = models.ForeignKey(Student, on_delete=models.RESTRICT, default=None)
    score = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"course: {self.course.lesson.name} -- student: {self.student.last_name}"
