"""
Overwriting Djangos builtin Management Commands.

"""
import sys
from pathlib import Path

from django.core.management.commands import startapp
from django.conf import settings

from ...inout import files


def camelcase(string: str) -> str:
    return ''.join([s.capitalize() for s in string.split('_')])


def replace_app_name(*, path: Path, suffix: str, pluralized: bool):
    """
    Replace the app_name in the HTML Templates
    suffix: '.djt' -> == 'html' or '.djhtml'
    (Django Templates, that use INSERT_APP_NAME_HERE and INSERT_CAMEL_CASE_APP_NAME_HERE)
    """
    templates_directory = path / 'templates' / f"{path.stem}"
    # remove the 's' from the end of the app_name if pluralized
    app_name = path.stem.rstrip('s') if pluralized else path.stem
    _files = [f for f in templates_directory.iterdir() if f.is_file() and f.suffix == suffix]
    for fp in _files:
        content = files.read_from_disk(path=fp)
        content = content.replace('INSERT_APP_NAME_HERE', app_name)
        content = content.replace('INSERT_CAMEL_CASE_APP_NAME_HERE', camelcase(app_name))
        files.write_to_disk(path=fp, content=content)


class Command(startapp.Command):

    def add_arguments(self, parser):
        parser.add_argument('--replace-html', action='store_true', help='Also replace the app_name in HTML Templates')
        parser.add_argument('--pluralize-name', action='store_true', help='Keep the app name without the "s"')
        super().add_arguments(parser=parser)

    def handle(self, *args, **options):
        """
        Overwrite the handle method to add the app to the apps directory
        """
        # options
        replace_html = options.get('replace_html', False)
        pluralize_name = options.get('pluralize_name', False)
        _directory = options.get('directory') or options.get('name')

        apps = Path(f'{settings.APPS_DIR}')
        app = apps / f'{_directory}s' if pluralize_name else apps / f"{_directory}"
        app.mkdir(exist_ok=True)

        options['directory'] = f"{app.resolve()}"

        if apps in [Path(p) for p in sys.path]:
            sys.path = [p for p in sys.path if Path(p) != apps]

        super().handle(*args, **options)
        if replace_html:
            replace_app_name(path=app, suffix='.djt', pluralized=pluralize_name)
