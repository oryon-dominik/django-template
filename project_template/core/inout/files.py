from pathlib import Path


def read_from_disk(path: Path) -> str:
    """
    Read from a file.
    Return the content of the file as a string.
    """
    try:
        with open(path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Template {path} does not exist.")
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return ''


def write_to_disk(path: Path, content: str):
    """Write to a file."""
    try:
        with open(path, 'w') as file:
            file.write(content)
    except FileNotFoundError:
        print(f"Template {path} does not exist.")
    except IOError as e:
        print(f"An error occurred while reading the file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
