import click
from .data import hotkeys

@click.command(help='List all available hotkeys')
def hotkeys_command():
  width = max(len(hotkey.shortcut) for hotkey in hotkeys)

  click.echo('Hotkeys:')

  for hotkey in hotkeys:
    click.echo(f'  {hotkey.shortcut:<{width}} | {hotkey.description}')
