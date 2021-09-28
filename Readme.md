# Library
Онлайн-библиотека

## Install (for Ubuntu)
1. Сначала необходимо установить редис-сервер для кэширования.
* sudo apt-get install redis-server
2. Клонируем проект, активируем виртуальное окружение и устанавливаем зависимости
* git clone https://github.com/RitisBarauskas/library.git
* cd library
* python3 -m venv venv
* . venv/bin/activate
* pip install -r requirements.txt
3. Создаем базу данных
* python manage.py makemigrations
* python manage.py migrate
4. Подгружаем фикстуры с начальными данными:
* python manage.py loaddata < librarydata.json
* python manage.py createsuperuser
5. Запуск проекта
* python manage.py runserver

## API Documentation
library/ - Постраничный вывод книг и авторов
library/authors/ - список авторов
library/authors/1 - вывод автора по id (например, 1)
library/books/ - список книг
library/books/2 - вывод книги по id (например, 2)

## Author
Ritis Barauskas

