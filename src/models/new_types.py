from typing import NewType

import httpx

__all__ = ('HTTPClient', 'HTML')

HTTPClient = NewType('HTTPClient', httpx.Client)
HTML = NewType('HTML', str)
