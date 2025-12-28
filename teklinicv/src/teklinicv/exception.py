from dataclasses import dataclass, field


@dataclass
class TekliniCVValidationError:
    location: tuple[str, ...]
    yaml_location: tuple[tuple[int, int], tuple[int, int]] | None
    message: str
    input: str


@dataclass
class TekliniCVUserError(ValueError):
    message: str | None = field(default=None)


@dataclass
class TekliniCVUserValidationError(ValueError):
    validation_errors: list[TekliniCVValidationError]


@dataclass
class TekliniCVInternalError(RuntimeError):
    message: str
