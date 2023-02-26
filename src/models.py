from dataclasses import dataclass

__all__ = ('ConnectAuthorizeFormData',)


@dataclass(frozen=True, slots=True)
class ConnectAuthorizeFormData:
    client_id: str
    redirect_uri: str
    response_type: str
    scope: str
    code_challenge: str
    code_challenge_method: str
    response_mode: str
    nonce: str
    state: str
