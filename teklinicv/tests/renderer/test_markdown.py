import pytest

from teklinicv.renderer.markdown import generate_markdown
from teklinicv.schema.models.teklinicv_model import TekliniCVModel


@pytest.mark.parametrize("cv_variant", ["minimal", "full"])
def test_generate_markdown(
    compare_file_with_reference,
    cv_variant: str,
    request: pytest.FixtureRequest,
):
    base_model = request.getfixturevalue(f"{cv_variant}_teklinicv_model")

    model = TekliniCVModel(
        cv=base_model.cv,
        locale=base_model.locale,
        settings=base_model.settings,
    )

    def generate_file(output_path):
        model.settings.render_command.markdown_path = output_path
        generate_markdown(model)

    reference_filename = f"{cv_variant}.md"
    assert compare_file_with_reference(generate_file, reference_filename)
