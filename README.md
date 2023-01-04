# django-template

> Project And App Structure for Django

This repository contains two templates: one for a project structure and one for an app structure.

You can use these by referring to their release files during project/app creation.

Project:

    django-admin startproject --template https://github.com/oryon-dominik/django-template/releases/download/latest/project_template.zip --extension=py,md,toml,. <project_name> <directory>

You can call it with your local python with

    python -c 'import os;import sys;from pathlib import Path;os.system(str((Path(sys.executable).parent / \"Scripts\" / \"django-admin\").resolve()) + \" startproject --template https://github.com/oryon-dominik/django-template/releases/download/latest/project_template.zip --extension=py,md,toml,. <project_name> .\")'

Default App (will be created in the project's `apps` folder):

    python manage.py startapp --template https://github.com/oryon-dominik/django-template/releases/download/latest/app_template_default.zip --extension=py,md,toml,. <app_name>

Rest App (will be created in the project's `apps` folder):

    python manage.py startapp --template https://github.com/oryon-dominik/django-template/releases/download/latest/app_template_rest.zip --extension=py,md,toml,. <app_name>


## Credits

[<3 shezi](https://github.com/shezi/django-better-project-template)
