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
- Tenant apps via [django-tenant-schemas](https://github.com/bernardopires/django-tenant-schemas).
    - __Organization__ model is the tenant base.
    - `core` app is shared (in `public` schema).
    - Use `migrate_schemas` instead of built-in `migrate` command.
    - Custom middleware to select `schema_name` from the request's header (`X-DTS-HEADER`). Default schema is `public`.

## Usage

You must have installed Django on your system to use `django-admin` command.

1. Create a new project by running:
```
django-admin startproject --template https://github.com/christianmtr/my_django_template/archive/master.zip --extensions=py,json new_django_project .
```

2. Create and active an virtual environment:
```
python -m venv venv
source venv/bin/activate
```
> Only works with Python 3.X, use `python3` if is necessary.

3. Change the database parameters in `settings.py` at line 77.

4. Install dependencies from `requirements.txt` by running:
```
pip install -r requirements.txt 
```
 
5. Create migration files:
```
python manage.py makemigrations
```

6. Apply migrations:
```
python manage.py migrate_schemas
```

7. Create `public` tenant:
```
python manage.py loaddata organization 
```

8. Create own organization:
```
python manage.py create_public_organization
```

8. Create a super user specifying `schema` name:
```
python manage.py createsuperuser
```

9. Run project:
```
python manage.py runserver
```

10. Enjoy =)


## Other behaviours and more features

Check out the other branches.
