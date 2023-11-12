from pathlib import Path, WindowsPath, PosixPath
from typing import Literal, TypeAlias

from django.urls import (
    URLResolver,
    URLPattern,
)


URLType: TypeAlias = URLResolver | URLPattern

PathType: TypeAlias = Path | WindowsPath | PosixPath

# DjangoMode is a generic, because it has no dependencies on Django itself.
DjangoMode: TypeAlias = Literal["test", "develop", "production"]
DjangoModeOrNone: TypeAlias = DjangoMode | None
