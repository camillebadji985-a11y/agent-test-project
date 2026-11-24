# todo

A small command-line to-do list manager written in Python (no external dependencies).

## Installation

```
git clone https://github.com/<your-account>/agent-test-project.git
cd agent-test-project
```

Requires Python 3.10 or later.

## Usage

| Command | Effect |
|---|---|
| `python -m todo add "title"` | Add a task |
| `python -m todo list` | Show all tasks |
| `python -m todo done <id>` | Mark a task as done |
| `python -m todo remove <id>` | Remove a task |

Tasks are saved in `~/.todo.json`. Set the `TODO_FILE` environment variable to use another file.

## Tests

```
python -m pytest
```
