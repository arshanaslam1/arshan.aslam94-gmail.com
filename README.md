# MarkFlow

For barq Dev

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

License: MIT

## Settings

Moved to [settings](https://cookiecutter-django.readthedocs.io/en/latest/1-getting-started/settings.html).

## Basic Commands

### Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create a **superuser account**, use this command:

      $ docker compose -f docker-compose.yml -f docker-compose.local.yml
- To create run migrations and create a superuser:

      $ docker compose -f docker-compose.yml -f docker-compose.local.yml run --rm django python manage.py migrate
      $ docker compose -f docker-compose.yml -f docker-compose.local.yml run --rm django python manage.py createsuperuser


- to see api documentation go to /swagger
- to see api documentation go to /redoc
      ```http://localhost:8000/api/docs/```
