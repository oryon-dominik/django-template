# maintenance

## direct access

1. ssh into the server

```bash
ssh -i <path-to-key> <adminusername>@<server-host> -p <server-port>
```

For administative tasks the <adminusername> executes `sudo` commands.  
The appuser `{{ project_name }}` is used to run the application. It has no privileges.

2. sudo to appuser `{{ project_name }}`

```bash
sudo su - {{ project_name }}

# From here you can call project commands. Envs are loaded already.
git pull
poetry install
python manage.py shell
...
# The application should usally log to ./logs/* from here.
```

3. See the daemon(s) logs

```bash
sudo journalctl -u {{ project_name }}
sudo journalctl -u {{ project_name }}tasks
```

4. Restarting the daemon(s)

```bash
sudo systemctl restart {{ project_name }}
sudo systemctl restart {{ project_name }}tasks
```

5. Caddy webserver

```bash
sudo systemctl status caddy
sudo cat /etc/caddy/Caddyfile
```
