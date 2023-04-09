from dataclasses import dataclass

__all__ = ('OfficeManagerAccount',)


@dataclass(frozen=True, slots=True)
class OfficeManagerAccount:
    name: str
    login: str
    password: str
