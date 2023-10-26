## server

### setup
- python -m venv venv
- source venv/bin/activate
- pip install Django
- pip install djangorestframework
- django-admin startproject core <name_project>

- python manage.py startapp <name_file>

### database
- python manage.py makemigrations <name_file>
- python manage.py migrate

### run
- python manage.py runserver

## library
- pip freeze > requirements.txt
- pip install -r requirements.txt

## static file
- python manage.py collectstatic