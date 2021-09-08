import django.utils.timezone
from django.db import models
from Education.models import StudyField, Student


# Create your models here.


class Book(models.Model):
    study_field = models.ForeignKey(StudyField, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    rented = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Rent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.RESTRICT)
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)
    active = models.BooleanField(default=True)
    date = models.DateField(default=django.utils.timezone.now)

    def __str__(self):
        return f'{self.student.user.username} -- {self.book.name}'

    def days_left(self):
        start_date = self.date
        end_date = start_date.replace(day=start_date.day + 30)
        delta = end_date - start_date
        return delta.days
