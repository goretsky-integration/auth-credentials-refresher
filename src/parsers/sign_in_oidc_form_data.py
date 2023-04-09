from bs4 import BeautifulSoup

import models

__all__ = ('parse_sign_in_oidc_form_data',)


def parse_sign_in_oidc_form_data(
        sign_in_oidc_form_html: models.HTML,
) -> models.SignInOidcFormData:
    required_credentials_names = ('code', 'scope', 'state', 'session_state')

    soup = BeautifulSoup(sign_in_oidc_form_html, 'lxml')

    tags_with_credentials = soup.find_all(
        attrs={'name': required_credentials_names},
    )
    sign_in_oidc_form_data = {
        tag['name']: tag['value']
        for tag in tags_with_credentials
    }
    return models.SignInOidcFormData(**sign_in_oidc_form_data)
