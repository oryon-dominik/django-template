import multiprocessing

# The number of Gunicorn worker processes to spawn. This number should be roughly
# twice the number of CPU cores available.
workers = multiprocessing.cpu_count() * 2 + 1

# The type of worker to use
# gthread = Thread-based workers
# sync = Syncronous workers
# gevent = Coroutine-based workers
# eventlet = Coroutine-based workers
worker_class = 'gthread'  # or 'sync' if you're using an older version of Gunicorn

# The number of worker threads for handling requests
threads = 2

# The host and port on which Gunicorn should listen
bind = '127.0.0.1:8000'

# The path to your Django project's WSGI application
wsgi_app = 'config.wsgi:application'
