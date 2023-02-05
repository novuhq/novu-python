"""This module is used to defined an abstract class for all reusable methods to communicate with the Novu API"""
import copy
import logging
from json.decoder import JSONDecodeError
from typing import Optional

import requests
import sentry_sdk

from novu.config import NovuConfig

LOGGER = logging.getLogger(__name__)


class Api:  # pylint: disable=R0903
    """Base class for all API in the Novu client"""

    def __init__(self, url: Optional[str] = None, api_key: Optional[str] = None) -> None:
        config = NovuConfig()

        url = url or config.url
        api_key = api_key or config.api_key

        self._url = url
        self._headers = {"Authorization": f"ApiKey {api_key}"}

    def handle_request(
        self,
        method: str,
        url: str,
        json: Optional[dict] = None,
        payload: Optional[dict] = None,
        headers: Optional[dict] = None,
        **kwargs,
    ) -> dict:
        """Handle a request to the API.

        This method can handle all cases of request and is used to authenticate the request and raise
        an error on bad status.

        Args:
            method: The HTTP method used during the request (e.g. "POST")
            url: The URL to reach during the request
            json: The body to send, in json format. Defaults to None.
            payload: Params to send, in json format. Defaults to None.
            headers: Headers to send, in json format. Defaults to None.

        Returns:
            Return parsed response.
        """
        if headers:
            _headers = copy.deepcopy(self._headers)
            _headers.update(copy.deepcopy(headers))
        else:
            _headers = self._headers

        res: requests.Response = requests.request(
            method=method,
            url=url,
            headers=_headers,
            json=json,
            params=payload,
            timeout=5,
            **kwargs,
        )

        if not res.ok:
            try:
                detail = res.json()
                # FIXME: For some reason, coverage doesn't see this line as covered.
                sentry_sdk.set_extra("error_details", detail)  # pragma: no cover
            except JSONDecodeError:
                pass
            res.raise_for_status()

        return res.json()
