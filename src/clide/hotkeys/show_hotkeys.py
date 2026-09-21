# cli.py
import click
from .data import HOTKEY_SECTIONS

@click.command()
@click.option('--apps', '-a', is_flag=True, help='Show application hotkeys.')
@click.option('--system', '-s', is_flag=True, help='Show system hotkeys.')
@click.option('--window-management', '-wm', is_flag=True, help='Show window management hotkeys.')
def show_hotkeys(apps: bool, system: bool, window_management: bool) -> None:
    """List all hotkeys, or a specific category."""
    selected = {
        "apps": apps,
        "system": system,
        "window_management": window_management,
    }
    show_all = not any(selected.values())

    for name, section in HOTKEY_SECTIONS.items():
        if show_all or selected.get(name):
            click.secho(section.title, bold=True)
            for hotkey in section.hotkeys:
                click.echo(f"  {hotkey.keys:<25} {hotkey.description}")
