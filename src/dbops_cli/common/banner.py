"""Banner utilities for the CLI."""

import sys

from rich import print as rprint

LOGO = r"""
[bold cyan]
██████╗ ██████╗  ██████╗ ██████╗ ███████╗
██╔══██╗██╔══██╗██╔═══██╗██╔══██╗██╔════╝
██║  ██║██████╔╝██║   ██║██████╔╝███████╗
██║  ██║██╔══██╗██║   ██║██╔═══╝ ╚════██║
██████╔╝██████╔╝╚██████╔╝██║     ███████║
╚═════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚══════╝
[/]
[dim]Databricks operations command-line helper[/]
"""


def opt_print_banner() -> None:
    """
    Prints the banner if help is requested.
    Example: `dbops --help` or `dbops jobs --help`, etc.
    """
    if any(arg in ("--help", "-h") for arg in sys.argv):
        rprint(LOGO)
