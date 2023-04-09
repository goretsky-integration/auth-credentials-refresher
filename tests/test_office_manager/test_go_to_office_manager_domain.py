import models


def test_go_to_office_manager_domain(httpx_mock, office_manager):
    httpx_mock.add_response(text=models.HTML('response'))
    connect_authorize_form_html = office_manager.go_to_office_manager_domain()
    assert connect_authorize_form_html == models.HTML('response')
