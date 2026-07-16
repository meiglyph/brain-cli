from datetime import date
from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(no_args_is_help=True)
console = Console()

NOTES_DIR = Path("notes")


@app.callback()
def main():
    """Brain CLI - a tiny tool for organizing thoughts in Markdown."""
    pass


@app.command()
def new(text: str):
    """Add a note to today's Markdown file."""
    NOTES_DIR.mkdir(exist_ok=True)

    today = date.today().isoformat()
    note_path = NOTES_DIR / f"{today}.md"

    with note_path.open("a", encoding="utf-8") as file:
        file.write(f"- {text}\n")

    console.print(f"Added note to {note_path}")


@app.command("list")
def list_notes():
    """List all note files."""
    if not NOTES_DIR.exists():
        console.print("No notes found.")
        return

    files = sorted(NOTES_DIR.glob("*.md"))

    if not files:
        console.print("No notes found.")
        return

    table = Table(title="Notes")
    table.add_column("File")

    for file in files:
        table.add_row(file.name)

    console.print(table)


@app.command()
def show(filename: str = typer.Argument(None)):
    """Show a note file. If no filename is given, show today's note."""
    if filename is None:
        filename = f"{date.today().isoformat()}.md"

    note_path = NOTES_DIR / filename

    if not note_path.exists():
        console.print(f"Note not found: {note_path}")
        raise typer.Exit(code=1)

    console.print(note_path.read_text(encoding="utf-8"))
