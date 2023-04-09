import models


def test_send_account_login_form_data(httpx_mock, dodo_is_auth):
    httpx_mock.add_response(text=models.HTML('response'))
    account_login_form_data = models.FilledAccountLoginFormData(
        username='login',
        password='password',
        tenant_name='dodopizza',
        country_code='kg',
        auth_method='local',
        remember_login=True,
        return_url='http://localhost:8000/',
        request_verification_token='jsdgjsibfuhsgnvsdfksd'
    )
    sign_in_oidc_form_html = dodo_is_auth.send_account_login_form_data(
        account_login_form_data=account_login_form_data,
    )
    assert sign_in_oidc_form_html == models.HTML('response')
