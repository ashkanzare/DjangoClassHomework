from django.urls import path

from library.api.views import BookViewSet

urlpatterns = [
    path('books-api/<str:text>', BookViewSet.as_view(), name='books_api'),
]




