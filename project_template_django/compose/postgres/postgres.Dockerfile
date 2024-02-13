FROM postgres:15

COPY init.sql /container-entrypoint-initdb.d/
COPY pg_hba.conf /opt/postgres/
COPY postgresql.conf /opt/postgres/

# RUN apt-get update && apt-get install postgresql-15-pgvector --assume-yes
