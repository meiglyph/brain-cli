from datetime import date

import pytest
from typer.testing import CliRunner

import brain.cli as cli
from brain.cli import app


runner = CliRunner()


@pytest.fixture
def notes_dir(tmp_path, monkeypatch):
    notes_path = tmp_path / "notes"
    monkeypatch.setattr(cli, "NOTES_DIR", notes_path)
    return notes_path


def test_help():
    result = runner.invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "Brain CLI" in result.stdout


def test_add_note(notes_dir):
    result = runner.invoke(app, ["add", "Learn pytest"])

    note_path = notes_dir / f"{date.today().isoformat()}.md"

    assert result.exit_code == 0
    assert note_path.exists()
    assert note_path.read_text(encoding="utf-8") == "- Learn pytest\n"


def test_list_without_notes(notes_dir):
    result = runner.invoke(app, ["list"])

    assert result.exit_code == 0
    assert "No notes found." in result.stdout


def test_show_missing_note(notes_dir):
    result = runner.invoke(app, ["show", "missing"])

    assert result.exit_code == 1
    assert "Note not found:" in result.stdout
    assert "missing.md" in result.stdout


def test_show_existing_note(notes_dir):
    notes_dir.mkdir()
    note_path = notes_dir / "example.md"
    note_path.write_text("- Test note\n", encoding="utf-8")

    result = runner.invoke(app, ["show", "example"])

    assert result.exit_code == 0
    assert "- Test note" in result.stdout


def test_search_finds_matching_note(notes_dir):
    notes_dir.mkdir()
    note_path = notes_dir / "example.md"
    note_path.write_text(
        "- Learn Python\n- Buy milk\n",
        encoding="utf-8",
    )

    result = runner.invoke(app, ["search", "python"])

    assert result.exit_code == 0
    assert "example.md" in result.stdout
    assert "- Learn Python" in result.stdout
    assert "Buy milk" not in result.stdout
