from dataclasses import dataclass

__all__ = ('AccountLoginConfig',)


@dataclass(frozen=True, slots=True)
class AccountLoginConfig:
    country_code: str
    remember_login: bool
