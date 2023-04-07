from dataclasses import dataclass

__all__ = ('SelectRoleFormData',)


@dataclass(frozen=True, slots=True)
class SelectRoleFormData:
    request_verification_token: str
