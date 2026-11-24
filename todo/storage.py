"""Save and load tasks from a JSON file."""

import json
from pathlib import Path

from .models import Task


def load_tasks(path: Path) -> list[Task]:
    if not path.exists():
        return []
    with open(path, encoding="utf-8") as f:
        return [Task.from_dict(item) for item in json.load(f)]


def save_tasks(path: Path, tasks: list[Task]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        json.dump([t.to_dict() for t in tasks], f, indent=2)
