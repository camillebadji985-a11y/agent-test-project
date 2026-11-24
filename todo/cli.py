"""Command-line interface: python -m todo <command> [arguments]."""

import argparse

from .config import get_data_file
from .models import Task
from .storage import load_tasks, save_tasks


def add_task(tasks: list[Task], title: str) -> Task:
    new_id = max((t.id for t in tasks), default=0) + 1
    task = Task(id=new_id, title=title)
    tasks.append(task)
    return task


def mark_done(tasks: list[Task], task_id: int) -> Task | None:
    """Mark a task as done. Return None if the id does not exist."""
    for task in tasks:
        if task.id == task_id:
            task.done = True
            return task
    return None


def remove_task(tasks: list[Task], task_id: int) -> None:
    tasks[:] = [t for t in tasks if t.id != task_id]


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(prog="todo", description="A small to-do list manager")
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("list", help="show all tasks")
    p_add = sub.add_parser("add", help="add a task")
    p_add.add_argument("title")
    p_done = sub.add_parser("done", help="mark a task as done")
    p_done.add_argument("id", type=int)
    p_rm = sub.add_parser("remove", help="remove a task")
    p_rm.add_argument("id", type=int)
    args = parser.parse_args(argv)

    path = get_data_file()
    tasks = load_tasks(path)

    if args.command == "list":
        if not tasks:
            print("No tasks yet.")
        for t in tasks:
            print(f"[{'x' if t.done else ' '}] {t.id}. {t.title}")
    elif args.command == "add":
        task = add_task(tasks, args.title)
        print(f"Added task {task.id}: {task.title}")
    elif args.command == "done":
        task = mark_done(tasks, args.id)
        if task is None:
            print(f"No task with id {args.id}.")
        else:
            print(f"Task {task.id} done.")
    elif args.command == "remove":
        remove_task(tasks, args.id)
        print(f"Task {args.id} removed.")

    save_tasks(path, tasks)
