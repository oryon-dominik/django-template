# TLDR

## Develop with me (on a postgres+redis setup)

```powershell
# Install dependencies.
poetry install

# Add large file storage support.
git lfs install

# Activate the virtual environment.
...

# Setup your `envs/develop.env` and `envs/test.env` from `envs/template.djt` or `doppler.com`.
# Just change (DJANGO_SETTINGS_MODULE=config.settings.test) for the test-environment.

# Install pre-commit hooks.
pre-commit install

# Spawn the containers (postgres+ redis).
podman compose -f containers/compose.yaml up

# Run the migrations and create the cache-table for sessions.
python manage.py migrate
python manage.py createcachetable

# Start the server (shortcut: cc up).
# See status on: http://127.0.0.1:8000/api/
python commands.py up

# Validate if everything works fine: run the tests.
pytest

# Add yourself to the contributors list after you made your first commit.
contributors-txt --aliases .\config\contributors\aliases.json
```

Now run the `notebooks/setup.ipynb` to create your first user.
