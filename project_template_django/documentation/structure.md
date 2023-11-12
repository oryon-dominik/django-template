# Project structure

    {{ project_name }}/
    ├── apps/                       # django apps
    ├── assets/                     # assets & static files
    ├── compose/                    # docker-compose files (postgres, ...)
    ├── config/                     # django project
    │   ├── settings/               # django settings
    │   │   ├── base/               # modularized base settings
    │   │   ├── environment/        # environment setup
    │   │   ├── develop.py          # develop settings
    │   │   ├── production.py       # production settings
    │   │   └── tests.py            # test settings
    │   ├── urls/                   # django urls
    │   │   ├── apis.py             # api routes
    │   │   ├── converters.py       # custom url converters
    │   │   └── routes.py           # django basic url-routes
    │   ├── startup.py              # startup script
    │   └── wsgi.py                 # wsgi script
    ├── core/                       # core app, shared over multiple projects
    ├── database/                   # sqlite database
    ├── documentation/
    ├── envs/                       # environment variables
    ├── frontend/                   # frontend framework
    ├── logs/
    ├── media/                      # media files (user uploads, ...)
    ├── notebooks/                  # jupyter notebooks for debugging
    ├── templates/                  # django base templates
    ├── test/
    │   ├── factories/              # factories for users ...
    │   ├── fixtures/               # fixtures for authentication, restframework, ...
    │   ├── tests/                  # actual global tests
    │   ├── clients.py              # test clients
    │   └── runners.py              # pytest runner for django
    ├── .gitignore                  # gitignore
    ├── .pre-commit-config.yaml     # pre-commit hooks
    ├── commands.py                 # project commands
    ├── manage.py                   # django manage
    ├── Procfile                    # heroku procfile, also used for describing production commands
    ├── pyproject.toml              # poetry project
    └── README.md                   # the
