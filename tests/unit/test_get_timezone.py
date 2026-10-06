import os
import subprocess
from unittest.mock import MagicMock, patch

import pytest

from clide.commands.timezones.get_timezone import get_timezone

SUBPROCESS_RUN = 'clide.commands.timezones.get_timezone.subprocess.run'


def fake_completed_process(stdout: str = 'Tue  6 Oct 21:04:12 JST 2026\n') -> MagicMock:
  process = MagicMock()
  process.stdout = stdout
  return process


class TestGetTimezoneCallsDate:
  def test_runs_the_date_command(self):
    with patch(SUBPROCESS_RUN, return_value=fake_completed_process()) as mock_run:
      get_timezone('Asia/Tokyo')

    assert mock_run.call_args.args[0] == ['date']

  def test_sets_tz_environment_variable_to_requested_zone(self):
    with patch(SUBPROCESS_RUN, return_value=fake_completed_process()) as mock_run:
      get_timezone('Asia/Tokyo')

    assert mock_run.call_args.kwargs['env']['TZ'] == 'Asia/Tokyo'

  def test_preserves_existing_environment_variables(self, monkeypatch):
    monkeypatch.setenv('CLIDE_TEST_VARIABLE', 'kept')

    with patch(SUBPROCESS_RUN, return_value=fake_completed_process()) as mock_run:
      get_timezone('Asia/Tokyo')

    assert mock_run.call_args.kwargs['env']['CLIDE_TEST_VARIABLE'] == 'kept'

  def test_overrides_an_existing_tz_value(self, monkeypatch):
    monkeypatch.setenv('TZ', 'America/New_York')

    with patch(SUBPROCESS_RUN, return_value=fake_completed_process()) as mock_run:
      get_timezone('Asia/Tokyo')

    assert mock_run.call_args.kwargs['env']['TZ'] == 'Asia/Tokyo'

  def test_does_not_modify_the_current_process_environment(self, monkeypatch):
    monkeypatch.setenv('TZ', 'Europe/London')

    with patch(SUBPROCESS_RUN, return_value=fake_completed_process()):
      get_timezone('Asia/Tokyo')

    assert os.environ['TZ'] == 'Europe/London'

  def test_captures_output_as_text_and_checks_exit_code(self):
    with patch(SUBPROCESS_RUN, return_value=fake_completed_process()) as mock_run:
      get_timezone('Asia/Tokyo')

    kwargs = mock_run.call_args.kwargs
    assert kwargs['capture_output'] is True
    assert kwargs['text'] is True
    assert kwargs['check'] is True


class TestGetTimezoneHandlesOutput:
  def test_returns_a_string(self):
    with patch(SUBPROCESS_RUN, return_value=fake_completed_process()):
      result = get_timezone('Asia/Tokyo')

    assert isinstance(result, str)

  def test_strips_surrounding_whitespace(self):
    with patch(SUBPROCESS_RUN, return_value=fake_completed_process('  some output \n\n')):
      result = get_timezone('Asia/Tokyo')

    assert result == 'some output'

  def test_returns_the_command_output(self):
    expected = 'Tue  6 Oct 21:04:12 JST 2026'

    with patch(SUBPROCESS_RUN, return_value=fake_completed_process(expected + '\n')):
      result = get_timezone('Asia/Tokyo')

    assert result == expected


class TestGetTimezoneErrors:
  def test_propagates_called_process_error(self):
    error = subprocess.CalledProcessError(returncode=1, cmd=['date'])

    with patch(SUBPROCESS_RUN, side_effect=error):
      with pytest.raises(subprocess.CalledProcessError):
        get_timezone('Asia/Tokyo')

  def test_propagates_file_not_found_when_date_is_missing(self):
    with patch(SUBPROCESS_RUN, side_effect=FileNotFoundError):
      with pytest.raises(FileNotFoundError):
        get_timezone('Asia/Tokyo')
