import models


def test_send_connect_authorize_form_data(httpx_mock, dodo_is_auth):
    httpx_mock.add_response(text=models.HTML('response'))

    connect_authorize_form_data = models.ConnectAuthorizeFormData(
        client_id='dodo-office-manager',
        redirect_uri='https://officemanager.dodois.test/signin-oidc',
        response_type='code',
        scope='openid employee profile ext_profile roles email phone users'
              ' offline_access dodo_staff_api accounting.admin inventory.admin',
        code_challenge='8P2Z86HaIIjufOF6aHoNTfcOxAr1avliDvxMF6Osn9w',
        code_challenge_method='S256',
        response_mode='form_post',
        nonce='638166445933971612.NWUyZjllMjEtNjYwYi00ZjdjLThmODEtNzMwMjhhYzFhZ'
              'DY4YWJiYWYzMzAtZjI5NC00NjIyLWE3YzktN2I5NGU5ZmVlY2Q3',
        state='CfDJ8JIVAtoTAL1Bq_ajCWf_96wpVumcVwOaVU2eYgRqmLoGOh_ZzS102HERnmbr'
              'MOGtFg3cwL2NaM2fbu29f2OfDO-5daeOAW6dDmnqD5l0rpQatWZUPOPmBxZspxAC'
              'exUAtrQcOxUTCoOmy6naCPHvpRlqN0MlRlaFvwPRLNmY5Nh7ncvgAxDFOPv4vuPO'
              'g5t9q_pp03sEg1H8iGMwbYQKX3hdSjlTgc7Q5qRLdaJ5mhnPY1j8IhVJ4CT3ZHmQ'
              'a_H-OKaoSfMfwkT34Tvp88fUxLC3WcMKeetT283ODOlbl9djp91JKlBxyII5IM7n'
              'AUbTj2l2r51jpD0wLT0z-U1jEleZQNcHiuvNk1NJQxHxjYCJDK7UpIiE4rayJjUU'
              'I4JnlQ'
    )
    account_login_form_html = dodo_is_auth.send_connect_authorize_form_data(
        connect_authorize_form_data=connect_authorize_form_data
    )
    assert account_login_form_html == models.HTML('response')
