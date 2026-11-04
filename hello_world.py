#!/usr/bin/env python3
"""A tiny command-line "Hello, World!" program.

Run it with no arguments to greet the world::

    python3 hello_world.py

Pass a name to greet someone specific::

    python3 hello_world.py Alice
"""

from __future__ import annotations

import argparse
import sys
from typing import Optional, Sequence

DEFAULT_NAME = "World"


def greet(name: str = DEFAULT_NAME) -> str:
    """Return the greeting for *name*.

    >>> greet()
    'Hello, World!'
    >>> greet("Alice")
    'Hello, Alice!'
    """
    name = name.strip()
    if not name:
        raise ValueError("name must not be empty")
    return f"Hello, {name}!"


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""
    parser = argparse.ArgumentParser(description="Print a friendly greeting.")
    parser.add_argument(
        "name",
        nargs="?",
        default=DEFAULT_NAME,
        help=f"who to greet (default: {DEFAULT_NAME})",
    )
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    """Run the command-line interface and return an exit code."""
    args = build_parser().parse_args(argv)
    try:
        print(greet(args.name))
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
