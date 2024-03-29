from bs4 import BeautifulSoup

import models

__all__ = ('parse_connect_authorize_form_data',)


def parse_connect_authorize_form_data(
        connect_authorize_form_html: models.HTML,
) -> models.ConnectAuthorizeFormData:
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

    soup = BeautifulSoup(connect_authorize_form_html, 'lxml')

    tags_with_credentials = soup.find_all(
        attrs={'name': required_credentials_names},
    )
    connect_authorize_form_data = {
        tag['name']: tag['value']
        for tag in tags_with_credentials
    }
    return models.ConnectAuthorizeFormData(**connect_authorize_form_data)
