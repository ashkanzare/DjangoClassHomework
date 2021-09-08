from rest_framework import generics
from .serializers import BookSerializer
from ..models import Book


# Create your views here.
class BookViewSet(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        text = self.kwargs['text']
        queryset = Book.objects.filter(name__contains=text)
        return queryset
