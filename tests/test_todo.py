from todo.cli import add_task, clear_done, mark_done, remove_task
from todo.storage import load_tasks, save_tasks


def test_add_and_done():
    tasks = []
    add_task(tasks, "write report")
    add_task(tasks, "read paper")
    assert [t.id for t in tasks] == [1, 2]
    mark_done(tasks, 2)
    assert tasks[1].done


def test_remove():
    tasks = []
    add_task(tasks, "a")
    add_task(tasks, "b")
    remove_task(tasks, 1)
    assert [t.title for t in tasks] == ["b"]


def test_save_and_load(tmp_path):
    path = tmp_path / "tasks.json"
    tasks = []
    add_task(tasks, "x")
    save_tasks(path, tasks)
    assert load_tasks(path)[0].title == "x"


def test_clear_done():
    tasks = []
    add_task(tasks, "a")
    add_task(tasks, "b")
    tasks[0].done = True
    assert clear_done(tasks) == 1
    assert [t.title for t in tasks] == ["b"]
