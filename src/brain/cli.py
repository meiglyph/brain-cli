from datetime import date
from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(no_args_is_help=True)
console = Console()

NOTES_DIR = Path.home() / ".brain-cli" / "notes"

@app.callback()
def main() -> None:
    """Brain CLI - a tiny tool for organizing thoughts in Markdown."""
    pass


@app.command("add")
def add_note(text: str) -> None:
    """Add a note to today's Markdown file."""
    NOTES_DIR.mkdir(parents=True, exist_ok=True)

    today = date.today().isoformat()
    note_path = NOTES_DIR / f"{today}.md"

    with note_path.open("a", encoding="utf-8") as file:
        file.write(f"- {text}\n")

    console.print(f"Added note to {note_path}")


@app.command("list")
def list_notes() -> None:
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
def show(filename: str | None = typer.Argument(None)) -> None:
    """Show a note file. If no filename is given, show today's note."""
    if filename is None:
        filename = f"{date.today().isoformat()}.md"
    elif not filename.endswith(".md"):
        filename = f"{filename}.md"

    note_path = NOTES_DIR / filename

    if not note_path.exists():
        console.print(f"Note not found: {note_path}")
        raise typer.Exit(code=1)

    console.print(note_path.read_text(encoding="utf-8"))


@app.command()
def search(query: str) -> None:
    """Search all notes for matching text."""
    if not NOTES_DIR.exists():
        console.print("No notes found.")
        raise typer.Exit(code=1)

    files = sorted(NOTES_DIR.glob("*.md"))
    normalized_query = query.casefold()
    matches_found = False

    for file in files:
        matching_lines = []

        for line in file.read_text(encoding="utf-8").splitlines():
            if normalized_query in line.casefold():
                matching_lines.append(line)

        if matching_lines:
            matches_found = True
            console.print(f"\n[bold]{file.name}[/bold]")

            for line in matching_lines:
                console.print(f"  {line}")

    if not matches_found:
        console.print(f'No notes matched "{query}".')
