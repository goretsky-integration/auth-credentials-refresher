from dataclasses import dataclass

__all__ = ('EmptyAccountLoginFormData', 'FilledAccountLoginFormData')


@dataclass(frozen=True, slots=True)
class EmptyAccountLoginFormData:
    return_url: str
    request_verification_token: str


@dataclass(frozen=True, slots=True)
class FilledAccountLoginFormData(EmptyAccountLoginFormData):
    username: str
    password: str
    tenant_name: str
    country_code: str
    auth_method: str
    remember_login: bool
