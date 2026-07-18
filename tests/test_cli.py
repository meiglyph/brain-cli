from typer.testing import CliRunner

from brain.cli import app


runner = CliRunner()


def test_help():
    result = runner.invoke(app, ["--help"])

    assert result.exit_code == 0
    assert "Brain CLI" in result.stdout

