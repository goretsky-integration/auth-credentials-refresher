from dataclasses import dataclass

__all__ = ('OfficeManagerAuthFormCredentials',)


@dataclass(frozen=True, slots=True)
class OfficeManagerAuthFormCredentials:
    client_id: str
    redirect_uri: str
    response_type: str
    scope: str
    code_challenge: str
    code_challenge_method: str
    response_mode: str
    nonce: str
    state: str
