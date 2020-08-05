# My Django project

This is a Django project template with all necessary stuff to run a functional project without more changes.

## Features

- Organization model with some basic attributes.
- User model (from Abstract model) with foreign key to Organization model.

## Usage

You must have installed Django on your system to use `django-admin` command.

1. Create a new project by running:
```
django-admin startproject --template https://github.com/christianmtr/my_django_template/archive/master.zip new_django_project .
```

2. Change the database backend in `settings.py` at line 72 and it parameters.

3. Create migration files:
```
python manage.py makemigrations
```

4. Apply migrations:
```
python manage.py migrate
```
5. Run project:

```
python manage.py runserver
```

 