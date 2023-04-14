# -- Modular settings ---------------------------------------------------------
# These settings are imported in the __init__.py of the base directory explicitly.
# To add a new setting, also edit the __init__.py
# -----------------------------------------------------------------------------
import sys
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent.parent.parent
APPS_DIR = ROOT_DIR / "apps"

# make sure our apps & config directories are on the python path
# This allows easy placement of apps within the interior apps directory.
sys.path.append(f'{ROOT_DIR / "apps"}')
sys.path.append(f'{ROOT_DIR / "config"}')
sys.path.append(f'{ROOT_DIR / "core"}')
sys.path.append(f'{ROOT_DIR / "test"}')
