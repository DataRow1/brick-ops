"""Exit handling utilities for the CLI."""

import typer

from dbops_cli.common.output import out


def ok_exit(msg: str | None = None) -> "None":
    """Exit successfully with an optional informational message."""
    if msg:
        out.info(msg)
    raise typer.Exit(0)


def die(msg: str, code: int = 1) -> "None":
    """Exit with an error message and optional exit code."""
    out.error(msg)
    raise typer.Exit(code)


def warn_exit(msg: str, code: int = 0) -> "None":
    """Exit with a warning message and optional exit code."""
    out.warn(msg)
    raise typer.Exit(code)
