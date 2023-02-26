import pathlib

import pytest

import models
from parsers import parse_connect_authorize_form_data


@pytest.fixture
def connect_authorize_form_data() -> str:
    with open(pathlib.Path(__file__).parent / 'connect_authorize_form_data.html', encoding='utf-8') as file:
        return file.read()


def test_connect_authorize_form_data_parser(connect_authorize_form_data):
    expected = models.ConnectAuthorizeFormData(
        client_id="dodo-office-manager",
        redirect_uri="https://officemanager.dodopizza.ru/signin-oidc",
        response_type="code",
        scope="openid employee profile ext_profile roles email phone users offline_access dodo_staff_api accounting.admin inventory.admin",
        code_challenge="oUMiRff7HyuRgdBq-VCMGIjUhOrO_CkxFydlB8hFvLo",
        code_challenge_method="S256",
        response_mode="form_post",
        nonce="638122174866445880.NDEyYjlhNzgtZGRlYy00YTI2LWJmYjctM2M0ZDc1NGQ1MzQwYTc2ZDQzNmUtNmFhMy00ZjQ3LWE5YTctZmU4NzAyMzg3Yjk3",
        state="CfDJ8KueySvRrKtEn0pZo9WUzAkboumxEXC44kbFovt5jkAmowGjrkvLXWxd8MHpqFQShd4HrVI5dTt0YmP13p1UF1x0cZd1igch-dWZpvjyxe0IlgbCBEdT7obwpAv2yeUA-DkOrfZbHuwY5z0h7uonl3LgY1M4w-cdaZF7vpz4QGXTKsmUGa9cnNW1HzgE4ZY9hFN7K7AkOoVWwSI7ItV46nH-5f6PoZkFxNbAKq8Oar64AyvshUeZEzJ420py2J4n0AIJZDA_2MOoadF0mkfba5RrdGr5GO-iO_ITvpd5onGqWEyj-tMRv69ZgdYreKHrAW5bw6YhrjzdHBC223kq7m9MI5q0apGxvcbLdC3sJqf_SeualWINMWE303pN4sV3YUKZPZuNOgEOyNWkxJTpYmM",
    )
    assert parse_connect_authorize_form_data(connect_authorize_form_data) == expected
