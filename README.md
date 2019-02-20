# Modular user model for Django
[![PyPI version](https://badge.fury.io/py/django-modular-user.svg)](https://badge.fury.io/py/django-modular-user)

**django-modular-user** lets you easily customize Django's User model, without any compromises. Unlike Django's own `AbstractBaseUser`, here nothing is irremovable, you can use exactly the parts you want.

## Requirements
* Django 2.0+

## Installation
```sh
pip install django-modular-user
```

* Create a new Django package with following models.py, and a migrations/ subdirectory:
```python
from django_modular_user.user import AbstractUser

class User(AbstractUser):
    pass
```

* In `settings.py`, set `AUTH_USER_MODEL = 'your_new_package_name.User'`
* Run `./manage.py makemigrations`

## Configuration
You may configure the basic profile data with `USER_CORE_MODULES` setting. For example, to create an User model without usernames and passwords, that uses email as the username, you may use:
```python
USER_CORE_MODULES = [
    'django_modular_user.user:AbstractBaseUser',
    'django_modular_user.user:EmailMixin', # email
    'django_modular_user.user:NamePartsMixin', # given_name, middle_name, family_name
    'django_modular_user.user:ActiveMixin', # is_active
    'django_modular_user.user:StaffMixin', # is_staff
    'django_modular_user.user:PermissionsMixin', # is_superuser and other permissions
    'django_modular_user.user:JoinedMixin', # date_joined
]
USERNAME_FIELD = 'email'
USER_EMAIL_UNIQUE = True
```

## App-specific User mixins
`django-modular-user` automatically scans all `INSTALLED_APPS` for `user.py` modules that contain a `UserMixin` class. Such mixins are automatically added to the User model; you only need to run `./manage.py makemigrations` after adding an app to your `INSTALLED_APPS` list.
