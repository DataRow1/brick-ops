"""Output formatting utilities for the CLI."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable, Mapping

from rich.console import Console
from rich.table import Table
from rich.theme import Theme

_THEME = Theme(
    {
        "ok": "bold green",
        "warn": "yellow",
        "err": "bold red",
        "title": "bold cyan",
        "meta": "dim",
    }
)

console = Console(theme=_THEME)


@dataclass(frozen=True)
class Out:
    """Output formatter for CLI messages and tables."""

    def info(self, msg: str) -> None:
        """Print an info message."""
        console.print(f"[title]›[/] {msg}")

    def success(self, msg: str) -> None:
        """Print a success message."""
        console.print(f"[ok]✓[/] {msg}")

    def warn(self, msg: str) -> None:
        """Print a warning message."""
        console.print(f"[warn]⚠[/] {msg}")

    def error(self, msg: str) -> None:
        """Print an error message."""
        console.print(f"[err]✗[/] {msg}")

    def header(self, title: str) -> None:
        """Print a header message."""
        console.print(f"[title]{title}[/]")

    def kv(self, items: Mapping[str, Any]) -> None:
        """Print key-value pairs."""
        for k, v in items.items():
            console.print(f"[meta]{k}[/]: {v}")

    def jobs_table(self, jobs: Iterable[Any], title: str = "Jobs") -> None:
        """
        Expects objects with .id .name .tags (like db_ops.core.models.Job)
        """
        t = Table(title=title, show_lines=False)
        t.add_column("Job ID", style="ok", no_wrap=True)
        t.add_column("Name")
        t.add_column("Tags", style="meta")

        for j in jobs:
            tags = ", ".join(
                f"{k}={v}" for k, v in (getattr(j, "tags", None) or {}).items()
            )
            t.add_row(str(j.id), j.name, tags)

        console.print(t)


out = Out()
