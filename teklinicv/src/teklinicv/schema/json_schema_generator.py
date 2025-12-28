import json
import pathlib

import pydantic

from teklinicv import __description__

from .models.teklinicv_model import TekliniCVModel


def generate_json_schema() -> dict:
    """Generate JSON Schema (Draft-07) from TekliniCV Pydantic models.

    Why:
        IDEs and validators need machine-readable schema for autocompletion
        and real-time validation. Custom generator adds TekliniCV-specific
        metadata like title, description, and canonical schema URL.

    Returns:
        Draft-07 JSON Schema dictionary.
    """

    class TekliniCVSchemaGenerator(pydantic.json_schema.GenerateJsonSchema):
        def generate(self, schema, mode="validation"):
            json_schema = super().generate(schema, mode=mode)
            json_schema["title"] = "TekliniCV"
            json_schema["description"] = __description__
            json_schema["$id"] = (
                "https://raw.githubusercontent.com/teklinicv/teklinicv/main/schema.json"
            )
            json_schema["$schema"] = "http://json-schema.org/draft-07/schema#"
            return json_schema

    return TekliniCVModel.model_json_schema(schema_generator=TekliniCVSchemaGenerator)


def generate_json_schema_file(json_schema_path: pathlib.Path) -> None:
    """Generate and save JSON Schema to file.

    Args:
        json_schema_path: Target file path for schema output.
    """
    schema = generate_json_schema()
    schema_json = json.dumps(schema, indent=2, ensure_ascii=False)
    json_schema_path.write_text(schema_json, encoding="utf-8")
