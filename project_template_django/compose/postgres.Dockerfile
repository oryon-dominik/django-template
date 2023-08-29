FROM postgres:15

COPY init.sql /docker-entrypoint-initdb.d/
COPY pg_hba.conf /opt/postgres/
COPY postgresql.conf /opt/postgres/
