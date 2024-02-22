# Start the gunicorn server for {{ project_name }}.
# -----------------------------------------------------------------------------
# --name requires 'setproctitle' to be installed in the venv.
# --worker-class=WORKERCLASS
# https://docs.gunicorn.org/en/stable/settings.html#worker-class

/apps/{{ project_name }}/src/.venv/bin/gunicorn --workers=4 --bind=0.0.0.0:8000 --name={{ project_name }} config.wsgi:application
