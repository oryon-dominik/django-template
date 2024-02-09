# How-to-postgres

## in develop

postgres settings might be better set inside the local.env instead of develop.env 
if you're using your own postgres instance

these settings get injected into the postgres docker, before you build
if you change them, you need to rebuild the postgres docker (and remove the old volume)

    docker compose down
    docker container rm {{ project_name }}_postgres
    docker volume rm {{ project_name }}_postgres_data


## in production

(obviously) don't use `POSTGRES_HOST_AUTH_METHOD=trust` when using the compose file `postgres.yml`.


## config

Have a look at the config files (postgres 15)

    docker exec -it {{ project_name }}_postgres cat /var/lib/postgresql/data/postgresql.conf
    docker exec -it {{ project_name }}_postgres cat /var/lib/postgresql/data/pg_hba.conf


## add an extension

Ensure your migrations are installed in the postgres system. For some you need an updated `Dockerfile`.
sometimes it's as easy as just replacing the baseimages in the compose files with `image: ankane/pgvector`.

Create an empty migration. Then add the extension to the migration file.
```bash
python manage.py makemigrations chat --name postgres_extension_pgvector --empty
```

```python
from django.contrib.postgres.operations import CreateExtension
# Some of the extensions are available in django.contrib.postgres.operations as direct imports.

operations = [
    CreateExtension('vector'),
]
```
Migrate :)
