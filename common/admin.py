from django.contrib.admin import ModelAdmin, register

from .models import Author, Book, Extra


@register(Author)
class AuthorAdmin(ModelAdmin):
    """Регистрация в админке автора"""

    list_display = ('id', 'first_name', 'second_name', 'birthday')
    empty_value_display = '-пусто-'


@register(Book)
class BookAdmin(ModelAdmin):
    """Регистрация в админке книг"""

    list_display = ('id', 'title', 'author')
    empty_value_display = '-пусто-'


@register(Extra)
class ExtraAdmin(ModelAdmin):
    """Регистрация в админке дополнительной информации о книгах"""

    list_display = ('id', 'book', 'extra_info')
    empty_value_display = '-пусто-'
