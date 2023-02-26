from bs4 import BeautifulSoup

import models

__all__ = (
    'parse_connect_authorize_form_data',
)


def parse_connect_authorize_form_data(auth_form_html: str) -> models.ConnectAuthorizeFormData:
    soup = BeautifulSoup(auth_form_html, 'lxml')
    required_credentials_names = (
        'client_id',
        'redirect_uri',
        'response_type',
        'scope',
        'code_challenge',
        'code_challenge_method',
        'response_mode',
        'nonce',
        'state',
    )
    tags_with_credentials = soup.find_all(attrs={'name': required_credentials_names})
    connect_authorize_form_data = {tag['name']: tag['value'] for tag in tags_with_credentials}
    return models.ConnectAuthorizeFormData(**connect_authorize_form_data)
