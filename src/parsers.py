from bs4 import BeautifulSoup

import models


def parse_office_manager_auth_form(auth_form_html: str):
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
    auth_form_credentials = {tag['name']: tag['value'] for tag in tags_with_credentials}
    return models.OfficeManagerAuthFormCredentials(**auth_form_credentials)
