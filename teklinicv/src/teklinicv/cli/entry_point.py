"""Entry point for the TekliniCV CLI.

Why:
    Users might install TekliniCV with `pip install teklinicv` instead of
    `pip install teklinicv[full]`. This module catches that case and shows a helpful
    error message instead of a confusing `ImportError`.
"""

import sys


def entry_point() -> None:
    """Entry point for the TekliniCV CLI."""
    try:
        from .app import app as cli_app  # NOQA: PLC0415
    except ImportError:
        error_message = """
It looks like you installed TekliniCV with:

    pip install teklinicv

But TekliniCV needs to be installed with:

    pip install "teklinicv[full]"

Please reinstall with the correct command above.
"""
        sys.stderr.write(error_message)
        raise SystemExit(1) from None

    cli_app()
