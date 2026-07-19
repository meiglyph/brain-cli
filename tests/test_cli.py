from datetime import date

from typer.testing import CliRunner

from brain.cli import app


runner = CliRunner()


def test_help():
    result = runner.invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "Brain CLI" in result.stdout


def test_add_note(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    result = runner.invoke(app, ["add", "Learn pytest"])

    note_path = tmp_path / "notes" / f"{date.today().isoformat()}.md"

    assert result.exit_code == 0
    assert note_path.exists()
    assert note_path.read_text(encoding="utf-8") == "- Learn pytest\n"

def test_list_without_notes(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    result = runner.invoke(app, ["list"])

    assert result.exit_code == 0
    assert "No notes found." in result.stdout

def test_show_missing_note(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    result = runner.invoke(app, ["show", "missing"])

    assert result.exit_code == 1
    assert "Note not found: notes/missing.md" in result.stdout

def test_show_existing_note(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    notes_dir = tmp_path / "notes"
    notes_dir.mkdir()
    note_path = notes_dir / "example.md"
    note_path.write_text("- Test note\n", encoding="utf-8")

    result = runner.invoke(app, ["show", "example"])

    assert result.exit_code == 0
    assert "- Test note" in result.stdout

def test_search_finds_matching_note(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    notes_dir = tmp_path / "notes"
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

