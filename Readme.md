#Library

Онлайн-библиотека

## Install (for Ubuntu)
1. Сначала необходимо установить редис-сервер для кэширования.
* sudo apt-get install redis-server
2. Клонируем проект, активируем виртуальное окружение и устанавливаем зависимости
* git clone ...
* cd library
* python3 -m venv venv
* . venv/bin/activate
* pip install -r requirements.txt
3. Создаем базу данных и суперпользователя
* python manage.py makemigrations
* python manage.py migrate
* python manage.py createsuperuser
