import os

import pytest

from clide.commands.timezones.get_timezone import get_timezone

pytestmark = pytest.mark.skipif(
  os.name == 'nt',
  reason='requires a POSIX `date` command',
)


class TestGetTimezoneIntegration:
  @pytest.mark.parametrize(
    'zone, expected_abbreviations',
    [
      ('Asia/Tokyo', ['JST']),
      ('UTC', ['UTC']),
      ('Europe/London', ['GMT', 'BST']),
      ('America/New_York', ['EST', 'EDT']),
      ('Australia/Sydney', ['AEST', 'AEDT']),
    ],
  )
  def test_returns_local_time_for_valid_zone(self, zone, expected_abbreviations):
    result = get_timezone(zone)

    assert any(abbreviation in result for abbreviation in expected_abbreviations)

  def test_returns_a_single_line(self):
    result = get_timezone('Asia/Tokyo')

    assert '\n' not in result

  def test_different_zones_give_different_abbreviations(self):
    tokyo = get_timezone('Asia/Tokyo')
    utc = get_timezone('UTC')

    assert 'JST' in tokyo
    assert 'JST' not in utc

  def test_invalid_zone_does_not_raise_or_report_a_real_zone(self):
    # `date` ignores unknown TZ values and falls back to UTC rather than
    # failing, so the function cannot detect a typo such as 'Asia/Japan' [2].
    # The exact fallback output varies by platform, so only assert what is stable.
    result = get_timezone('Asia/Japan')

    assert isinstance(result, str)
    assert 'JST' not in result
