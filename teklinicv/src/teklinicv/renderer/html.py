import pathlib

from teklinicv.schema.models.teklinicv_model import TekliniCVModel

from .path_resolver import resolve_teklinicv_file_path
from .templater.templater import render_html


def generate_html(
    teklinicv_model: TekliniCVModel, markdown_path: pathlib.Path | None
) -> pathlib.Path | None:
    """Generate HTML file from Markdown source with styling.

    Why:
        HTML format enables web hosting and sharing CVs online. Converts
        Markdown to HTML body and wraps with CSS styling and metadata.

    Args:
        teklinicv_model: CV model for path resolution and rendering context.
        markdown_path: Path to Markdown source file.

    Returns:
        Path to generated HTML file, or None if generation disabled.
    """
    if (
        teklinicv_model.settings.render_command.dont_generate_html
        or markdown_path is None
    ):
        return None
    html_path = resolve_teklinicv_file_path(
        teklinicv_model, teklinicv_model.settings.render_command.html_path
    )
    html_contents = render_html(
        teklinicv_model, markdown_path.read_text(encoding="utf-8")
    )
    html_path.write_text(html_contents, encoding="utf-8")
    return html_path
