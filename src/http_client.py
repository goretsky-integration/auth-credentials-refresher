import contextlib

import httpx

__all__ = ('closing_http_client',)


@contextlib.closing
def closing_http_client(*, base_url: str) -> httpx.Client:
    headers = {'User-Agent': 'dodoextbot'}
    with httpx.Client(base_url=base_url, headers=headers) as client:
        yield client
