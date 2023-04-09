from dataclasses import dataclass

import models
from parsers import fill_account_login_form_data


@dataclass(frozen=True, slots=True)
class AccountLoginConfig:
    country_code: str
    remember_login: bool


def test_fill_account_login_form_data():
    empty_account_login_form_data = models.EmptyAccountLoginFormData(
        return_url='http://localhost:8000/',
        request_verification_token='jsdgjsibfuhsgnvsdfksd',
    )
    account = models.OfficeManagerAccount(
        name='office_manager_msk_0',
        login='login',
        password='password',
    )
    account_login_config = AccountLoginConfig(
        country_code='kg',
        remember_login=True,
    )
    actual = fill_account_login_form_data(
        empty_account_login_form_data=empty_account_login_form_data,
        office_manager_account=account,
        account_login_config=account_login_config,
    )
    expected = models.FilledAccountLoginFormData(
        username='login',
        password='password',
        tenant_name='dodopizza',
        country_code='kg',
        auth_method='local',
        remember_login=True,
        return_url='http://localhost:8000/',
        request_verification_token='jsdgjsibfuhsgnvsdfksd'
    )
    assert actual == expected
