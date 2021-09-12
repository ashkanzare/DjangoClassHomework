from django.core.management.base import BaseCommand, CommandError

from Education.models import StudentCourse
from library.models import Book


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'book-id',
            nargs='+',
            type=int,
            help='Make all books status to rented'
        )

    def handle(self, *args, **options):
        books = Book.objects.filter(id__in=options['book-id'])
        books.update(rented=True)
        self.stdout.write(self.style.SUCCESS('status of given book_id list changed to rented'))
