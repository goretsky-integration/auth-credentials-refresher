from typing import Protocol

from bs4 import BeautifulSoup

import models

__all__ = ('parse_account_login_form_data', 'fill_account_login_form_data')


class IAccountLoginConfig(Protocol):
    country_code: str
    remember_login: bool


def parse_account_login_form_data(
        account_login_form_html: models.HTML,
) -> models.EmptyAccountLoginFormData:
    soup = BeautifulSoup(account_login_form_html, 'lxml')

    return_url = soup.find(
        attrs={'name': 'ReturnUrl'},
    )['value']
    request_verification_token = soup.find(
        attrs={'name': '__RequestVerificationToken'},
    )['value']

    return models.EmptyAccountLoginFormData(
        return_url=return_url,
        request_verification_token=request_verification_token,
    )


def fill_account_login_form_data(
        *,
        empty_account_login_form_data: models.EmptyAccountLoginFormData,
        office_manager_account: models.OfficeManagerAccount,
        account_login_config: IAccountLoginConfig,
) -> models.FilledAccountLoginFormData:
    return models.FilledAccountLoginFormData(
        return_url=empty_account_login_form_data.return_url,
        request_verification_token=empty_account_login_form_data.request_verification_token,

        country_code=account_login_config.country_code,
        remember_login=account_login_config.remember_login,

        username=office_manager_account.login,
        password=office_manager_account.password,

        tenant_name='dodopizza',
        auth_method='local',
    )
