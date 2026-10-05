import click
import subprocess
from .get_timezone import get_timezone
from .data import timezones

@click.command(help='Show the time in personally meaningful locations.')
def timezones_command():
  labels = [f'{timezone.city}, {timezone.country}' for timezone in timezones]
  width = max(len(label) for label in labels)

  click.echo('Your timezones: \n')

  for timezone, label in zip(timezones, labels):
    time = get_timezone(timezone.zone)
    click.echo(f'  📍 {label:<{width}}: 🕓 {time}')
