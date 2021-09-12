from django.core.management.base import BaseCommand, CommandError

from Education.models import StudentCourse


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'student',
            help='Delete all courses of a student with student id or username'
        )

    def handle(self, *args, **options):
        global student_courses
        student_info = options['student']

        try:
            student_courses = StudentCourse.objects.filter(student_id=int(student_info))

        except ValueError:
            student_courses = StudentCourse.objects.filter(student__user__username=student_info)

        finally:
            if student_courses:
                student_courses.delete()
                self.stdout.write(self.style.SUCCESS('Courses of given student deleted successfully'))
            else:
                raise CommandError(f'Student with username/id : [{student_info}] does not exits.')
