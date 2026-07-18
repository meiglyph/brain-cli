# Brain CLI

A simple command-line note-taking tool built with Python, Typer, and Rich.

## Features

- Add notes from the command line
- Save notes as Markdown files by date
- List saved note files
- Show today's note or a selected note file
- Search all notes for matching text

## Installation

Clone the repository:

```bash
git clone git@github.com:meiglyph/brain-cli.git
cd brain-cli
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install Brain CLI in editable mode:

```bash
python -m pip install -e .
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

## Project Structure

```text
brain-cli/
├── examples/
│   └── example-note.md
├── notes/
├── src/
│   └── brain/
│       ├── __init__.py
│       └── cli.py
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

The `notes/` directory is ignored by Git so personal notes are not published.

## Built With

- Python
- Typer
- Rich

## License

This project is licensed under the MIT License.