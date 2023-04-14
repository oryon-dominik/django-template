from pathlib import Path

pd = Path(__file__).parent


def walk_directory_recursively_and_rename(directory: Path, source: str, target: str):
    """
    Walks through a directory recursively and renames all files with a given extension to another extension.
    """
    for path in directory.iterdir():
        if path.is_dir():
            walk_directory_recursively_and_rename(path, source, target)
        elif path.is_file() and path.suffix == source:
            path.rename(path.with_suffix(target))

# rename step 1: all py-tpl to py to format them
# rename step 2: all py to py-tpl to commit them again
walk_directory_recursively_and_rename(pd, '.py', '.py-tpl')
