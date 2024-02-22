
cd /apps/{{ project_name}}/src

/opt/python/bin/poetry config --local virtualenvs.in-project true  && \
/opt/python/bin/poetry install && \

/apps/{{ project_name }}/src/.venv/bin/python run python commands.py setup --production && \
/apps/{{ project_name }}/src/.venv/bin/python run python manage.py migrate

cd -
