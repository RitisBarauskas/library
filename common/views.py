from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from .serializers import AuthorSerializer, BookSerializer, BookListWithExtraSerializer
from .models import Author, Book, Extra
from .utils import OneResultOnPage


class AuthorViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()


class BookViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = BookSerializer
    queryset = Book.objects.all()


class BookListWithExtra(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = BookSerializer
    pagination_class = OneResultOnPage
    queryset = Book.objects.all()


