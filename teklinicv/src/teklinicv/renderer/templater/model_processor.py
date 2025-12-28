from collections.abc import Callable
from typing import Literal

from teklinicv.schema.models.cv.section import Entry
from teklinicv.schema.models.teklinicv_model import TekliniCVModel

from .connections import compute_connections
from .entry_templates_from_input import render_entry_templates
from .footer_and_top_note import render_footer_template, render_top_note_template
from .markdown_parser import markdown_to_typst
from .string_processor import apply_string_processors, make_keywords_bold


def process_model(
    teklinicv_model: TekliniCVModel, file_type: Literal["typst", "markdown"]
) -> TekliniCVModel:
    """Pre-process CV model for template rendering with format-specific transformations.

    Why:
        Templates need processed data, not raw model. This applies markdown
        parsing, keyword bolding, connection formatting, date rendering, and
        entry template expansion before templates execute.

    Args:
        teklinicv_model: Validated CV model.
        file_type: Target format for format-specific processors.

    Returns:
        Processed model ready for templates.
    """
    teklinicv_model = teklinicv_model.model_copy(deep=True)

    string_processors: list[Callable[[str], str]] = [
        lambda string: make_keywords_bold(string, teklinicv_model.settings.bold_keywords)
    ]
    if file_type == "typst":
        string_processors.extend([markdown_to_typst])

    teklinicv_model.cv.plain_name = teklinicv_model.cv.name  # ty: ignore[unresolved-attribute]
    teklinicv_model.cv.name = apply_string_processors(
        teklinicv_model.cv.name, string_processors
    )
    teklinicv_model.cv.headline = apply_string_processors(
        teklinicv_model.cv.headline, string_processors
    )
    teklinicv_model.cv.connections = compute_connections(teklinicv_model, file_type)  # ty: ignore[unresolved-attribute]
    teklinicv_model.cv.top_note = render_top_note_template(  # ty: ignore[unresolved-attribute]
        teklinicv_model.design.templates.top_note,
        locale=teklinicv_model.locale,
        current_date=teklinicv_model.settings.current_date,
        name=teklinicv_model.cv.name,
        single_date_template=teklinicv_model.design.templates.single_date,
        string_processors=string_processors,
    )

    teklinicv_model.cv.footer = render_footer_template(  # ty: ignore[unresolved-attribute]
        teklinicv_model.design.templates.footer,
        locale=teklinicv_model.locale,
        current_date=teklinicv_model.settings.current_date,
        name=teklinicv_model.cv.name,
        single_date_template=teklinicv_model.design.templates.single_date,
        string_processors=string_processors,
    )
    if teklinicv_model.cv.sections is None:
        return teklinicv_model

    for section in teklinicv_model.cv.teklinicv_sections:
        section.title = apply_string_processors(section.title, string_processors)
        show_time_span = (
            section.snake_case_title
            in teklinicv_model.design.sections.show_time_spans_in
        )
        for i, entry in enumerate(section.entries):
            entry = render_entry_templates(  # NOQA: PLW2901
                entry,
                templates=teklinicv_model.design.templates,
                locale=teklinicv_model.locale,
                show_time_span=show_time_span,
                current_date=teklinicv_model.settings.current_date,
            )
            section.entries[i] = process_fields(entry, string_processors)

    return teklinicv_model


def process_fields(
    entry: Entry, string_processors: list[Callable[[str], str]]
) -> Entry:
    """Apply string processors to all entry fields except skipped technical fields.

    Why:
        Entry fields need markdown parsing and formatting, but dates, DOIs, and
        URLs must remain unprocessed for correct linking and formatting. Field-
        level processing enables selective transformation.

    Args:
        entry: Entry to process (model or string).
        string_processors: Transformation functions to apply.

    Returns:
        Entry with processed fields.
    """
    skipped = {"start_date", "end_date", "doi", "url"}

    if isinstance(entry, str):
        return apply_string_processors(entry, string_processors)

    data = entry.model_dump(exclude_none=True)
    for field, value in data.items():
        if field in skipped or field.startswith("_"):
            continue

        if isinstance(value, str):
            setattr(entry, field, apply_string_processors(value, string_processors))
        elif isinstance(value, list):
            setattr(
                entry,
                field,
                [apply_string_processors(v, string_processors) for v in value],
            )
        else:
            setattr(
                entry, field, apply_string_processors(str(value), string_processors)
            )

    return entry
