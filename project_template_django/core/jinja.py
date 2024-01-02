from django.templatetags.static import static
from django.urls import reverse
from jinja2 import Environment
from django_browser_reload.jinja import django_browser_reload_script


"""
https://docs.djangoproject.com/en/4.2/topics/templates/#django.template.backends.jinja2.Jinja2

Set BACKEND to 'django.template.backends.jinja2.Jinja2' to configure a Jinja2 engine.
The most important entry in OPTIONS is 'environment'. It's a dotted Python path
to a callable returning a Jinja2 environment. It defaults to
'jinja2.Environment'. Django invokes that callable and passes other options as
keyword arguments. Furthermore, Django adds defaults that differ from Jinja2's
for a few options:


Render the tag in your base template. It can go anywhere, but it's best just before </body>:

    {% verbatim %}{{ django_browser_reload_script }}{% endverbatim %}

    <img src="{{ static('path/to/company-logo.png') }}" alt="Company Logo">
    <a href="{{ url('admin:index') }}">Administration</a>

    </body>
</html>
"""


def environment(**options):
    env = Environment(**options)
    env.globals.update(
        {
            "static": static,
            "url": reverse,
            "django_browser_reload_script": django_browser_reload_script,
        }
    )
    return env
