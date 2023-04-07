import contextlib

import httpx

import models

__all__ = ('closing_http_client',)


@contextlib.contextmanager
def closing_http_client(*, base_url: str) -> models.HTTPClient:
    if not base_url:
        raise ValueError('Base url is not provided')

    headers = {'User-Agent': 'dodoextbot'}
    with httpx.Client(base_url=base_url, headers=headers) as client:
        yield models.HTTPClient(client)
