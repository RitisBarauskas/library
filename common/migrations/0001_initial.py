# Generated by Django 3.2.7 on 2021-09-28 14:13

from django.db import migrations, models
import django.db.models.deletion
import picklefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name')),
                ('second_name', models.CharField(max_length=30, verbose_name='second name')),
                ('birthday', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='year birthday')),
            ],
            options={
                'verbose_name': 'author',
                'verbose_name_plural': 'authors',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='title book')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='title', to='common.author')),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
            },
        ),
        migrations.CreateModel(
            name='Extra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extra_info', picklefield.fields.PickledObjectField(editable=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extra', to='common.book', verbose_name='Extra information')),
            ],
            options={
                'verbose_name': 'Extra info',
                'verbose_name_plural': 'Extra info about books',
            },
        ),
    ]
