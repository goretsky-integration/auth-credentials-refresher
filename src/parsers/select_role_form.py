from bs4 import BeautifulSoup

import models

__all__ = ('parse_select_role_form',)


def parse_select_role_form(
        select_role_form_html: models.HTML,
) -> models.SelectRoleFormData:
    soup = BeautifulSoup(select_role_form_html, 'lxml')

    request_verification_token = soup.find(
        attrs={'name': '__RequestVerificationToken'},
    )['value']

    return models.SelectRoleFormData(
        request_verification_token=request_verification_token,
    )
