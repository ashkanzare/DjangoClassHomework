from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Book, Rent
from Education.models import Student
from Education.vars import INVALID_RENT_COUNT, RENT_REMAIN


def rent_book(request):
    std = Student.objects.get(user=request.user)
    std_books = Rent.objects.filter(student_id=std.id)
    if request.method == 'POST':
        books_id = request.POST.getlist('results[]')
        if request.is_ajax() and len(std_books) + len(books_id) <= 5:
            for i in books_id:
                new_rent, created = Rent.objects.get_or_create(student_id=std.id, book_id=int(i))
                if created:
                    new_rent.save()
            return redirect('Education:home')
        print(len(std_books) + len(books_id))
        messages.error(request, INVALID_RENT_COUNT)
        messages.error(request, RENT_REMAIN + f'{5 - len(std_books)}')
        return redirect('library:rent_book')
    context = {
        'std': std,
        'std_books': std_books
    }
    return render(request, 'library/rent-book.html', context=context)
