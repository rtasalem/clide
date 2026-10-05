import click
import subprocess
from .data import timezones

@click.command(help='Show the time in personally meaningful timezones.')
def timezones_command():

  click.echo('The time is...')

  for timezone in timezones:
    result = subprocess.run(['TZ=f"{timezone.country}/{timezone.city}"', 'date', ' > /dev/null 2>&1'])
    click.echo(f'The time in {timezone.city}, {timezone.country} is ')
