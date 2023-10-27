"""This module is used to defined an abstract class for all reusable methods to communicate with the Novu API"""
import copy
import dataclasses
import logging
import os
from json.decoder import JSONDecodeError
from typing import Generic, List, Optional, Type, TypeVar, Union
from uuid import uuid4

import requests
from tenacity import retry, stop_after_attempt, wait_chain, wait_exponential, wait_fixed

from novu.config import NovuConfig
from novu.dto.base import CamelCaseDto
from novu.helpers import SentryProxy

LOGGER = logging.getLogger(__name__)


_C_co = TypeVar("_C_co", bound=CamelCaseDto, covariant=True)


def retry_backoff(f):
    """Decorator to handle retry mechanism based on user configuration"""

    def wrapper(*args):
        retry_config: RetryConfig = args[0].retry_config

        if retry_config:
            func = retry(
                wait=wait_chain(
                    *[wait_fixed(retry_config.initial_delay)]
                    + [wait_exponential(min=retry_config.wait_min, max=retry_config.wait_max)]
                ),
                stop=stop_after_attempt(retry_config.retry_max),
            )(f)
        else:
            func: f

        return func(*args)

    return wrapper


class PaginationIterator(Generic[_C_co]):  # pylint: disable=R0902
    """The class is a generic iterator which allow to iterate directly on result without
    looking for pagination during handling.

    Args:
        api: The api used to call
        item_class: The Dto to parse each items return by API.
        url: The URL to query during fetch.
        payload: Payload to query during fetch.
    """

    def __init__(self, api: "Api", item_class: Type[_C_co], url: str, payload: Optional[dict] = None):
        self.__item_class = item_class
        self.__api = api
        self.__url = url
        self.__payload = payload or {}

        self.__has_more = False
        self.__page = 0
        self.__limit = 10
        self.__index = 0
        self.__buffer: List[_C_co] = []

        self.__payload["limit"] = self.__limit
        self.__payload["page"] = self.__page
        self.__fetch_data()

    def __iter__(self) -> "PaginationIterator[_C_co]":
        return self

    def __next__(self) -> _C_co:
        return self.next()

    def next(self) -> _C_co:
        """Implementation of the next behavior for the iterator."""
        if self.__index < len(self.__buffer):
            result, self.__index = self.__buffer[self.__index], self.__index + 1
            return result

        if self.__has_more:
            self.__fetch_data()

            result, self.__index = self.__buffer[self.__index], self.__index + 1
            return result

        raise StopIteration()

    def __fetch_data(self):
        self.__payload["page"] = self.__page
        self.__page += 1

        data = self.__api.handle_request(
            method="GET",
            url=self.__url,
            payload=self.__payload,
        )

        self.__has_more = data.get("hasMore", data.get("totalCount", 0) > (self.__page + 1 * self.__limit))
        self.__buffer = list(map(self.__item_class.from_camel_case, data.get("data", [])))
        self.__index = 0


@dataclasses.dataclass
class RetryConfig:  # pylint: disable=R0903
    """Configuration Class to add Exponential Retry Mechanism"""

    initial_delay: int
    """Initial delay for first retry"""

    wait_min: int
    """Minimum time to wait"""

    wait_max: int
    """Maximum time to wait"""

    retry_max: int
    """Maximum number of retries"""


class Api:  # pylint: disable=R0903
    """Base class for all API in the Novu client"""

    requests_timeout: int = 5
    """This field allow you to change the :param:`~requests.request.timeout` params which is used during API calls."""

    retry_config: Optional[RetryConfig] = None
    """This field allow you to add Exponential Retry Mechanism for API calls."""

    session: Optional[requests.Session] = None
    """This field allow you to use a :class:`~requests.Session` during API calls."""

    def __init__(
        self,
        url: Optional[str] = None,
        api_key: Optional[str] = None,
        requests_timeout: Optional[int] = None,
        retry_config: Optional[RetryConfig] = None,
        session: Optional[requests.Session] = None,
    ) -> None:
        config = NovuConfig()

        url = url or config.url
        api_key = api_key or config.api_key

        self._url = url
        self._headers = {"Authorization": f"ApiKey {api_key}", "Idempotency-Key": str(uuid4())}

        self.requests_timeout = requests_timeout or int(os.getenv("NOVU_PYTHON_REQUESTS_TIMEOUT", "5"))
        self.retry_config = retry_config
        self.session = session

    @retry_backoff
    def handle_request(
        self,
        method: str,
        url: str,
        json: Optional[Union[dict, list]] = None,
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

        res = (self.session.request if self.session else requests.request)(
            method=method,
            url=url,
            headers=_headers,
            json=json,
            params=payload,
            timeout=self.requests_timeout,
            **kwargs,
        )

        if not res.ok:
            try:
                detail = res.json()
                SentryProxy().set_extra("error_details", detail)
            except JSONDecodeError:
                pass
            res.raise_for_status()

        if res.status_code == 204:
            return {}

        return res.json()
