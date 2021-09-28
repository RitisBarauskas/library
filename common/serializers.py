from rest_framework.serializers import (CharField, IntegerField,
                                        ModelSerializer, SlugRelatedField,
                                        ValidationError)

from .models import Author, Book, Extra


class AuthorSerializer(ModelSerializer):
    """Author serializer."""

    class Meta:
        fields = fields = '__all__'
        model = Author


class BookSerializer(ModelSerializer):
    """Author serializer."""

    class Meta:
        fields = fields = '__all__'
        model = Book


class BookListWithExtraSerializer(ModelSerializer):
    """Book list with Extra info"""

    class Meta:
        fields = ('book', 'extra_info')
        model = Extra
