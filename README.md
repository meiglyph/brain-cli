# Brain CLI

A simple command-line note-taking tool built with Python, Typer, and Rich.

## Features

- Add notes from the command line
- Save notes as Markdown files by date
- List saved note files
- Show the contents of a selected note file

## Installation

Clone the repository and install it in editable mode:

```bash
git clone git@github.com:meiglyph/brain-cli.git
cd brain-cli
pip install -e .
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

Show a note file:

```bash
brain show 2026-07-08
```

View all available commands:

```bash
brain --help
```

## Project Structure

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

## Built With

- Python
- Typer
- Rich

## License

This project is licensed under the MIT License.