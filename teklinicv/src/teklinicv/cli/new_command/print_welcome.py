import rich
import rich.panel
from rich import print

from teklinicv import __version__


def print_welcome():
    """Display welcome banner with version and useful links.

    Why:
        New users need guidance on where to find documentation and support.
    """
    print(f"\nWelcome to [dodger_blue3]TekliniCV v{__version__}[/dodger_blue3]!\n")
    links = {
        "TekliniCV App": "https://teklinicv.com",
        "Documentation": "https://docs.teklinicv.com",
        "Source code": "https://github.com/teklinicv/teklinicv/",
        "Bug reports": "https://github.com/teklinicv/teklinicv/issues/",
    }
    link_strings = [
        f"[bold cyan]{title + ':':<15}[/bold cyan] [link={link}]{link}[/link]"
        for title, link in links.items()
    ]
    link_panel = rich.panel.Panel(
        "\n".join(link_strings),
        title="Useful Links",
        title_align="left",
        border_style="bright_black",
    )

    print(link_panel)
