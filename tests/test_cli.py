from click.testing import CliRunner
from clide.cli import cli

def test_version_long_flag():
  runner = CliRunner()
  result = runner.invoke(cli, ['--version'])

  assert result.exit_code == 0
  assert 'version' in result.output

def test_version_short_flag():
  runner = CliRunner()
  result = runner.invoke(cli, ['-v'])

  assert result.exit_code == 0
  assert 'version' in result.output
