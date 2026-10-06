from click.testing import CliRunner
from clide.cli import cli
from clide.commands.hotkeys.data import hotkeys

def test_hotkeys_command_lists_all_available_hotkeys():
# ensures the test fails when the `hotkeys` list is empty 
# i.e. makes sure the test is testing against data
  assert hotkeys

  runner = CliRunner()
  result = runner.invoke(cli, ['hotkeys'])

  assert result.exit_code == 0

  for hotkey in hotkeys:
    assert hotkey.shortcut in result.output
    assert hotkey.description in result.output

def test_hotkeys_command_aligns_dividers():
  runner = CliRunner()
  result = runner.invoke(cli, ['hotkeys'])

  lines = [line for line in result.output.splitlines() if ' | ' in line]
  divider_positions = {line.index(' | ') for line in lines}

  assert lines
  assert len(divider_positions) == 1
