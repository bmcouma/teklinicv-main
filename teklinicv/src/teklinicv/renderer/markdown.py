import pathlib

from teklinicv.schema.models.teklinicv_model import TekliniCVModel

from .path_resolver import resolve_teklinicv_file_path
from .templater.templater import render_full_template


def generate_markdown(teklinicv_model: TekliniCVModel) -> pathlib.Path | None:
    """Generate Markdown file from CV model via Jinja2 templates.

    Why:
        Markdown provides human-readable CV format for version control and
        web platforms. Acts as intermediate format for HTML generation.

    Args:
        teklinicv_model: Validated CV model with content.

    Returns:
        Path to generated Markdown file, or None if generation disabled.
    """
    if teklinicv_model.settings.render_command.dont_generate_markdown:
        return None
    markdown_path = resolve_teklinicv_file_path(
        teklinicv_model, teklinicv_model.settings.render_command.markdown_path
    )
    markdown_contents = render_full_template(teklinicv_model, "markdown")
    markdown_path.write_text(markdown_contents, encoding="utf-8")
    return markdown_path
