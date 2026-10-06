from click.testing import CliRunner
from clide.cli import cli
from clide.commands.timezones.data import timezones

def test_timezones_command_lists_all_timezones():
# ensures the test fails when the `timezones` list is empty 
# i.e. makes sure the test is testing against data
  assert timezones

  runner = CliRunner()
  result = runner.invoke(cli, ['timezones'])

  assert result.exit_code == 0

  for timezone in timezones:
    assert timezone.city in result.output
    assert timezone.country in result.output
