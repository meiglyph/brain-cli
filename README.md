# Brain CLI

[![Tests](https://github.com/meiglyph/brain-cli/actions/workflows/tests.yml/badge.svg)](https://github.com/meiglyph/brain-cli/actions/workflows/tests.yml)

A simple command-line note-taking tool built with Python, Typer, and Rich.

## Features

- Add notes from the command line
- Save notes as Markdown files by date
- List saved note files
- Show today's note or a selected note file
- Search all notes for matching text
- Store notes in a consistent location inside the user's home directory

## Requirements

- Python 3.10 or later

## Installation

Clone the repository:

```bash
git clone https://github.com/meiglyph/brain-cli.git
cd brain-cli
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install Brain CLI:

```bash
python -m pip install .
```

## Usage

Add a note:

```bash
brain add "Built my first CLI command."
```

List saved note files:

```bash
brain list
```

Show today's note:

```bash
brain show
```

Show a note from a specific date:

```bash
brain show 2026-07-18
```

Search all notes:

```bash
brain search SSH
```

View all available commands:

```bash
brain --help
```

## Note Storage

Notes are stored in the following directory inside the user's home directory:

```text
~/.brain-cli/notes/
```

This keeps personal notes separate from the cloned Git repository.

## Development

Install the project with development dependencies:

```bash
python -m pip install -e ".[dev]"
```

Run the test suite:

```bash
pytest -v
```

Tests also run automatically on GitHub Actions after every push and pull request.

## Project Structure

```text
brain-cli/
├── .github/
│   └── workflows/
│       └── tests.yml
├── examples/
│   └── example-note.md
├── src/
│   └── brain/
│       ├── __init__.py
│       └── cli.py
├── tests/
│   └── test_cli.py
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

## Built With

- Python
- Typer
- Rich
- pytest
- GitHub Actions

## License

This project is licensed under the MIT License.
