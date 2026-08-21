import click

version = None
param_decls = ['--version', '-v']

@click.group()
@click.version_option(version, *param_decls)
@click.pass_context
def cli(ctx):
  pass

if __name__ == '__main__':
  cli()
