# gbdamis

GBDA Membership Information System



License: MIT

## Settings

Moved to [settings](http://cookiecutter-django.readthedocs.io/en/latest/settings.html).

## Basic Commands

### Setting Up App

- To start, run pip install -r and  **requirements/local.txt**, If you use pipenv, you can activate a virtual environment and run pipenv install -r requirements/local.

- To run **local server**, use this command
    
      $python manage.py runserver --settings=config.settings.local

- To create a **superuser account**, use this command:

      $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

