import pytest

from teklinicv.renderer.pdf_png import generate_pdf, generate_png
from teklinicv.renderer.typst import generate_typst
from teklinicv.schema.models.design.built_in_design import available_themes
from teklinicv.schema.models.teklinicv_model import TekliniCVModel


@pytest.mark.parametrize("theme", available_themes)
@pytest.mark.parametrize("cv_variant", ["minimal", "full"])
def test_generate_pdf(
    compare_file_with_reference,
    theme: str,
    cv_variant: str,
    request: pytest.FixtureRequest,
):
    base_model = request.getfixturevalue(f"{cv_variant}_teklinicv_model")

    model = TekliniCVModel(
        cv=base_model.cv,
        design={"theme": theme},
        locale=base_model.locale,
        settings=base_model.settings,
    )

    def generate_file(output_path):
        model.settings.render_command.typst_path = output_path.with_suffix(".typ")
        typst_path = generate_typst(model)

        model.settings.render_command.pdf_path = output_path
        generate_pdf(model, typst_path)

    reference_filename = f"{theme}_{cv_variant}.pdf"

    assert compare_file_with_reference(generate_file, reference_filename)


@pytest.mark.parametrize("theme", available_themes)
def test_generate_png(
    compare_file_with_reference,
    theme: str,
    minimal_teklinicv_model: TekliniCVModel,
):
    model = TekliniCVModel(
        cv=minimal_teklinicv_model.cv,
        design={"theme": theme},
        locale=minimal_teklinicv_model.locale,
        settings=minimal_teklinicv_model.settings,
    )

    def generate_file(output_path):
        model.settings.render_command.typst_path = output_path.with_suffix(".typ")
        typst_path = generate_typst(model)

        model.settings.render_command.png_path = output_path
        generate_png(model, typst_path)

    reference_filename = f"{theme}_minimal.png"

    assert compare_file_with_reference(generate_file, reference_filename)
