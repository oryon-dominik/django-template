"""
Overwriting Djangos builtin Management Commands.

"""
import sys
from importlib import import_module
from pathlib import Path

from django.conf import settings
from django.core.management.base import CommandError
from django.core.management.commands import startapp

from ...inout import files


def camelcase(string: str) -> str:
    return "".join([s.capitalize() for s in string.split("_")])


def replace_app_name(*, path: Path, suffix: str, pluralized: bool):
    """
    Replace the app_name in the HTML Templates
    suffix: '.djt' -> == 'html' or '.djhtml'
    (Django Templates, that use INSERT_APP_NAME_HERE and INSERT_CAMEL_CASE_APP_NAME_HERE)
    """
    templates_directory = path / "templates" / f"{path.stem}"
    # remove the 's' from the end of the app_name if pluralized
    app_name = path.stem.rstrip("s") if pluralized else path.stem
    _files = [f for f in templates_directory.iterdir() if f.is_file() and f.suffix == suffix]
    for fp in _files:
        content = files.read_from_disk(path=fp)
        content = content.replace("INSERT_APP_NAME_HERE", app_name)
        content = content.replace("INSERT_CAMEL_CASE_APP_NAME_HERE", camelcase(app_name))
        files.write_to_disk(path=fp, content=content)


class Command(startapp.Command):
    def add_arguments(self, parser):
        parser.add_argument("--replace-html", action="store_true", help="Also replace the app_name in HTML Templates")
        parser.add_argument("--pluralize-name", action="store_true", help='Keep the app name without the "s"')
        super().add_arguments(parser=parser)

    def handle(self, *args, **options):
        """
        Overwrite the handle method to add the app to the apps directory
        """
        # options
        replace_html = options.get("replace_html", False)
        pluralize_name = options.get("pluralize_name", False)
        _directory = options.get("directory") or options.get("name")

        apps = Path(f"{settings.APPS_DIR}")
        app = apps / f"{_directory}s" if pluralize_name else apps / f"{_directory}"
        app.mkdir(exist_ok=True, parents=True)

        options["directory"] = f"{app.resolve()}"

        if apps in [Path(p) for p in sys.path]:
            sys.path = [p for p in sys.path if Path(p) != apps]

        self.a_or_an = "an"
        super().handle(*args, **options)
        if replace_html:
            replace_app_name(path=app, suffix=".djt", pluralized=pluralize_name)

    def validate_name(self, name, name_or_dir="name"):
        if name is None:
            raise CommandError(
                "you must provide {an} {app} name".format(
                    an=self.a_or_an,
                    app=self.app_or_project,
                )
            )
        # Check it's a valid directory name.
        if not name.isidentifier():
            raise CommandError(
                "'{name}' is not a valid {app} {type}. Please make sure the "
                "{type} is a valid identifier.".format(
                    name=name,
                    app=self.app_or_project,
                    type=name_or_dir,
                )
            )
        # Check it cannot be imported.
        try:
            import_module(name)
        except ImportError:
            pass
        else:
            if name != "users":
                # ! Monkey patch to allow another custom users app
                raise CommandError(
                    "'{name}' conflicts with the name of an existing Python "
                    "module and cannot be used as {an} {app} {type}. Please try "
                    "another {type}.".format(
                        name=name,
                        an=self.a_or_an,
                        app=self.app_or_project,
                        type=name_or_dir,
                    )
                )
