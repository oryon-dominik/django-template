# django-template

> Project And App Structure Templates for Django.

---

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

You can use these template by referring to their release files during project/app creation.  
Preinstalled `Django in your local python version is required.`  
Although this should be pretty self-explanatory, please remember to replace `<project_name>` and `<app_name>` with your project/app name ;-).


## Project:

    django-admin startproject --template https://github.com/oryon-dominik/django-template/releases/download/latest/project_template.zip --extension=py,md,toml,. <project_name> <directory>

You can call it with your local python with

    python -c 'import os;import sys;from pathlib import Path;os.system(str((Path(sys.executable).parent / \"Scripts\" / \"django-admin\").resolve()) + \" startproject --template https://github.com/oryon-dominik/django-template/releases/download/latest/project_template.zip --extension=py,md,toml,. <project_name> .\")'


For any subsequent command (creating apps..) *install the dependencies* and *activate your virtual environment*.


## Default App

(will be created in the project's `apps` folder)

    python manage.py startapp --template https://github.com/oryon-dominik/django-template/releases/download/latest/app_template_default.zip --extension=py,md,toml,. <app_name>


- Add `'apps.<app_name>.apps.<app_name.capitalize()>Config'` to `LOCAL_APPS` or `PROJECT_APPS` in `config.settings.base.py`.  
- Add the apps routes to `urlpatterns` in `config.urls.py` like this: `path('', include('apps.<app_name>.urls', namespace="<app_name>")),`  

## Rest App

(will be created in the project's `apps` folder)

    python manage.py startapp --template https://github.com/oryon-dominik/django-template/releases/download/latest/app_template_rest.zip --extension=py,md,toml,. <app_name>


- Add `'apps.<app_name>.apps.<app_name.capitalize()>Config'` to `LOCAL_APPS` or `PROJECT_APPS` in `config.settings.base.py`.  
- Add `'rest_framework'` to `THIRD_PARTY_APPS` in `config.settings.base.py`.  
- Add the apps routes to `urlpatterns` in `config.urls.py` like this: `path('', include('apps.<app_name>.api.urls', namespace="<app_name>")),`  


## Credits

[<3 shezi](https://github.com/shezi/django-better-project-template)
