# django-template

> Project And App Structure Templates for Django.

---

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

You can use these templates by referring to their release files during project/app creation.  
Preinstalled `Django in your local python version is required.`  
Although this should be pretty self-explanatory, please remember to replace `<project_name>` and `<app_name>` with your project/app name ;-).


## Project:

    django-admin startproject --template https://github.com/oryon-dominik/django-template/releases/download/latest/project_template.zip --extension=py,md,toml,. <project_name> <directory>

Local python version:

    python -c 'import os;import sys;from pathlib import Path;os.system(str((Path(sys.executable).parent / \"Scripts\" / \"django-admin\").resolve()) + \" startproject --template https://github.com/oryon-dominik/django-template/releases/download/latest/project_template.zip --extension=py,md,toml,. <project_name> .\")'


For any subsequent command (creating apps..) *install the dependencies* and *activate your virtual environment*.


## Default App

(will be created in the project's `apps` folder)

    python manage.py startapp --template https://github.com/oryon-dominik/django-template/releases/download/latest/app_template_default.zip --extension=py,md,toml,. <app_name>


- Add `'apps.<app_name>.apps.<app_name.capitalize()>Config'` to `LOCAL_APPS` or `PROJECT_APPS` in `config.settings.base.py`.  
- Add the apps routes to `urlpatterns` in `config.urls.py` like this: `path('', include('apps.<app_name>.urls', namespace="<app_name>")),`.  


## Rest App

(will be created in the project's `apps` folder)

    python manage.py startapp --template https://github.com/oryon-dominik/django-template/releases/download/latest/app_template_rest.zip --extension=py,md,toml,. <app_name>


- Add `'apps.<app_name>.apps.<app_name.capitalize()>Config'` to `LOCAL_APPS` or `PROJECT_APPS` in `config.settings.base.py`.  
- Add the apps routes to `urlpatterns` in `config.urls.py` like this: `path('', include('apps.<app_name>.api.urls', namespace="<app_name>")),`.  


## Authentication App for JWT

(will be created in the project's `apps` folder)

    python manage.py startapp --template https://github.com/oryon-dominik/django-template/releases/download/latest/app_template_authentication.zip --extension=py,md,toml,. authentication

- In `config.urls.api` comment `path('', include('apps.authentication.api.urls')),` in.

Authentication is checking blacklisted tokens (whitelisting is a BAD idea ;-P) and will have a slow default cache (database access) for production.
If you only use one worker, you might want to switch to memory for development.

    # for a database cache backend create the table
    python manage.py createcachetable


## Basic CRUD Templates Example App

(will be created in the project's `apps` folder, please use a singluar name, that will be automatically pluralized - it's a crud app after all ;-] )

    python manage.py startapp --template https://github.com/oryon-dominik/django-template/releases/download/latest/app_template_simple_crud_templates.zip --extension=py,md,toml,. --pluralize-name --replace-html <app_name>

- Add `'apps.<app_name>.apps.<app_name.capitalize()>Config'` to `LOCAL_APPS` or `PROJECT_APPS` in `config.settings.base.py`.  
- Add the apps routes to `urlpatterns` in `config.urls.py` like this: `path('', include('apps.<app_name>.api.urls', namespace="<app_name>")),`.  
- Edit your `models.py` accordingly and `makemigrations` and `migrate`.  


## Basic vuejs Templates Example App

(will be created in the project's `apps` folder, please use a singluar name, that will be automatically pluralized - it's a crud app after all ;-] )

    python manage.py startapp --template https://github.com/oryon-dominik/django-template/releases/download/latest/app_template_vuejs_templates.zip --extension=py,md,toml,. --pluralize-name --replace-html <app_name>

- Add `'apps.<app_name>.apps.<app_name.capitalize()>Config'` to `LOCAL_APPS` or `PROJECT_APPS` in `config.settings.base.py`.  
- Add the apps routes to `urlpatterns` in `config.urls.py` like this: `path('', include('apps.<app_name>.api.urls', namespace="<app_name>")),`.  



## Credits

[<3 shezi](https://github.com/shezi/django-better-project-template)
