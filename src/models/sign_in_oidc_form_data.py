from dataclasses import dataclass

__all__ = ('SignInOidcFormData',)


@dataclass(frozen=True, slots=True)
class SignInOidcFormData:
    code: str
    scope: str
    state: str
    session_state: str
