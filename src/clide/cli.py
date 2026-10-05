import click
from .commands.hotkeys.command import hotkeys_command
from .commands.timezones.command import timezones_command

version = None
param_decls = ['--version', '-v']

@click.group()
@click.version_option(version, *param_decls)
@click.pass_context
def cli(ctx):
  pass

cli.add_command(hotkeys_command)
cli.add_command(timezones_command)

if __name__ == '__main__':
  cli()
