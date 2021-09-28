from rest_framework.serializers import (CharField, IntegerField,
                                        ModelSerializer, SlugRelatedField,
                                        ValidationError)

from .models import Author, Book, Extra


class AuthorSerializer(ModelSerializer):
    """Author serializer."""

    class Meta:
        fields = 'first_name', 'second_name', 'birthday'
        model = Author


class BookSerializer(ModelSerializer):
    """Author serializer."""

    class Meta:
        fields = 'title', 'author'
        model = Book


class OneBookOnPageSerializer(ModelSerializer):
    """Book list"""

    author = AuthorSerializer(read_only=True, many=False)

    class Meta:
        fields = 'title', 'author'
        model = Book
