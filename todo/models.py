"""Data model for a task."""

from dataclasses import dataclass, asdict


@dataclass
class Task:
    id: int
    title: str
    done: bool = False

    def to_dict(self) -> dict:
        return asdict(self)

    @staticmethod
    def from_dict(data: dict) -> "Task":
        return Task(id=data["id"], title=data["title"], done=data.get("done", False))
