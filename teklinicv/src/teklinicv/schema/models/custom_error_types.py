from enum import Enum


class CustomPydanticErrorTypes(str, Enum):
    entry_validation = "teklinicv_entry_validation_error"
    other = "teklinicv_other_error"
