import click
from .show_hotkeys.hotkeys import show_hotkeys

version = None
param_decls = ['--version', '-v']

@click.group()
@click.version_option(version, *param_decls)
@click.pass_context
def cli(ctx):
  pass

cli.add_command(show_hotkeys)

if __name__ == '__main__':
  cli()
