import toml
from config.paths import ROOT_DIR

project = toml.load(ROOT_DIR / "pyproject.toml")

__application__ = project["tool"]["poetry"]["name"]
__version__ = project["tool"]["poetry"]["version"]
