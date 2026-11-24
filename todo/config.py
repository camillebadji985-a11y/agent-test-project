"""Configuration of the application."""

import os
from pathlib import Path

DEFAULT_FILE = Path.home() / ".todo.json"


def get_data_file() -> Path:
    """Return the file where tasks are stored (can be changed with TODO_FILE)."""
    return Path(os.environ.get("TODO_FILE", DEFAULT_FILE))
