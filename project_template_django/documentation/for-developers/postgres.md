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
