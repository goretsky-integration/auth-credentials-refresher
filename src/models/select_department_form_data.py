from dataclasses import dataclass

__all__ = ('SelectDepartmentFormData',)


@dataclass(frozen=True, slots=True)
class SelectDepartmentFormData:
    request_verification_token: str
