import httpx
import pytest

from http_client import closing_http_client


@pytest.mark.parametrize(
    'base_url',
    [
        '',
        None,
    ]
)
def test_invalid_base_url_passed(base_url):
    with pytest.raises(ValueError, match='Base url is not provided'):
        with closing_http_client(base_url=base_url) as http_client:
            pass


@pytest.mark.parametrize(
    'base_url, timeout',
    [
        ('http://localhost:7000', 10),
        ('http://localhost:9000', 50),
        ('http://localhost:2000', 1),
    ]
)
def test_http_client_factory(base_url, timeout):
    with closing_http_client(base_url=base_url, timeout=timeout) as http_client:
        assert http_client.base_url == base_url
        assert http_client.timeout == httpx.Timeout(timeout)
        assert http_client.headers['user-agent'] == 'dodoextbot'
