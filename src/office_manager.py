import httpx

__all__ = (
    'go_to_office_manager_domain',
)


def go_to_office_manager_domain(http_client: httpx.Client) -> str:
    response = http_client.get('/')
    return response.text
