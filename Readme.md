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
1. library/ - Постраничный вывод книг и авторов
2. library/authors/ - список авторов
3. library/authors/1 - вывод автора по id (например, 1)
4. library/books/ - список книг
5. library/books/2 - вывод книги по id (например, 2)

## Author
Ritis Barauskas

