from django.urls import path, reverse_lazy

from .views import BookViewSet, rent_book

app_name = 'library'


urlpatterns = [
    path('books-api/<str:text>', BookViewSet.as_view(), name='books_api'),
    path('rent-book/', rent_book, name='rent_book')
]




