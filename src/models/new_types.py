from typing import NewType

import httpx

__all__ = ('HTTPClient',)

HTTPClient = NewType('HTTPClient', httpx.Client)
