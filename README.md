# My Django project

This is a Django project template with all necessary stuff to run a functional project without more changes.

## Features

- Organization model with some basic attributes.
- User model (from Abstract model) with foreign key to Organization model.
- User's email to login (`username` field is copied from email).
- Rest API support:
    - Login. Obtain access token and refresh access token.
    - Return user info with tokens at login.
    - CORS headers allowing all hosts.
    - Swagger docs.

## Usage

You must have installed Django on your system to use `django-admin` command.

1. Create a new project by running:
```
django-admin startproject --template https://github.com/christianmtr/my_django_template/archive/master.zip new_django_project .
```

2. Create and active an virtual environment:
```
python -m venv venv
source venv/bin/activate
```
> Only works with Python 3.X, use `python3` if is necessary.

3. Change the database backend in `settings.py` at line 72 and it parameters.

4. Install dependencies from `requirements.txt` by running:
```
pip install -r requirements.txt 
```
> Install database driver if its necessary.
 
5. Create migration files:
```
python manage.py makemigrations
```

6. Apply migrations:
```
python manage.py migrate
```

7. Run project:
```
python manage.py runserver
```

8. Enjoy =)


## Other behaviours and more features

Check out the other branches.