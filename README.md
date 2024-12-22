# Социальная сеть для блогеров.

Проект работает и доступен по адресу - https://tatarenkov.pythonanywhere.com/

### Описание
Представляем социальную сеть для публикации личных дневников. 
### Технологии
Python 3.7
Django 2.2.19
### Запуск проекта в dev-режиме

### Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:a1go3/yatube.git
```

### Cоздать и активировать виртуальное окружение на Linux / Mac:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip

### Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

### Выполнить миграции:

```
cd api_yamdb
```
```
python3 manage.py migrate
```
### Запустить проект:

```
python3 manage.py runserver

```
