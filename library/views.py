from django.shortcuts import render, redirect
from rest_framework import generics
from .serializers import BookSerializer
from .models import Book, Rent
from Education.models import Student


# Create your views here.
class BookViewSet(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        text = self.kwargs['text']
        queryset = Book.objects.filter(name__contains=text)
        return queryset


def rent_book(request):
    std = Student.objects.get(user=request.user)
    if request.method == 'POST':
        if request.is_ajax():
            books_id = request.POST.getlist('results[]')
            for i in books_id:
                new_rent = Rent(student_id=std.id, book_id=int(i))
                new_rent.save()
            return redirect('Education:home')
    context = {
        'std': std
    }
    return render(request, 'library/rent-book.html', context=context)
