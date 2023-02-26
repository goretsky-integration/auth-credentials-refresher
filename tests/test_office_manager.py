import httpx

from office_manager import go_to_office_manager_domain


def test_go_to_office_manager_domain(httpx_mock):
    httpx_mock.add_response(html='<form></form>')

    with httpx.Client(base_url='http://localhost:8000') as client:
        assert go_to_office_manager_domain(client) == '<form></form>'
