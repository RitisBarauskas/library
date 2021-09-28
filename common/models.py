from django.db import models
from picklefield.fields import PickledObjectField


class Author(models.Model):
    """ Авторы книг """

    first_name = models.CharField(
        verbose_name='first name',
        max_length=30
    )

    second_name = models.CharField(
        verbose_name='second name',
        max_length=30
    )

    birthday = models.PositiveSmallIntegerField(
        verbose_name='year birthday',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'

    def __str__(self):
        return f'{self.first_name} {self.second_name}'


class Book(models.Model):
    """ Книги """

    title = models.CharField(
        verbose_name="title book",
        max_length=50
    )

    author = models.ForeignKey(
        Author,
        related_name='title',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'

    def __str__(self):
        return self.title


class Extra(models.Model):
    """ Дополнительная информация о книгах"""

    book = models.ForeignKey(
        Book,
        verbose_name='Extra information',
        on_delete=models.CASCADE,
        related_name='extra'
    )

    extra_info = PickledObjectField()

    class Meta:
        verbose_name = 'Extra info'
        verbose_name_plural = 'Extra info about books'

    def __str__(self):
        return self.book

