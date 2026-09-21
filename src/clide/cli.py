import click
from .commands.hotkeys.hotkeys import hotkeys

version = None
param_decls = ['--version', '-v']

@click.group()
@click.version_option(version, *param_decls)
@click.pass_context
def cli(ctx):
  pass

cli.add_command(hotkeys)

if __name__ == '__main__':
  cli()
