from dataclasses import dataclass

__all__ = ('AccountLoginFormData',)


@dataclass(frozen=True, slots=True)
class AccountLoginFormData:
    return_url: str
    username: str
    password: str
    tenant_name: str
    country_code: str
    auth_method: str
    remember_login: bool
    request_verification_token: str
