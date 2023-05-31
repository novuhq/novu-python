"""
This module is used to define the ``FeedApi``, a python wrapper to interact with ``Feeds`` in Novu.
"""
from typing import Iterator, Optional

import requests

from novu.api.base import Api
from novu.constants import FEEDS_ENDPOINT
from novu.dto.feed import FeedDto


class FeedApi(Api):
    """This class aims to handle all API methods around feeds in Novu"""

    def __init__(
        self,
        url: Optional[str] = None,
        api_key: Optional[str] = None,
        requests_timeout: Optional[int] = None,
        session: Optional[requests.Session] = None,
    ) -> None:
        super().__init__(url=url, api_key=api_key, requests_timeout=requests_timeout, session=session)

        self._feed_url = f"{self._url}{FEEDS_ENDPOINT}"

    def list(self) -> Iterator[FeedDto]:
        """List existing feeds

        Yields:
            Mapped feed
        """
        results = self.handle_request("GET", self._feed_url)["data"]
        for result in results:
            yield FeedDto.from_camel_case(result)

    def create(self, name: str) -> FeedDto:
        """Create a new feed using it's name

        Args:
            name: The name of the feed to create

        Returns:
            Mapped created feed
        """
        return FeedDto.from_camel_case(self.handle_request("POST", self._feed_url, {"name": name})["data"])

    def delete(self, feed_id: str) -> FeedDto:
        """Remove a feed using it's identifier

        Args:
            feed_id: The feed identifier

        Returns:
            Mapped deleted feed
        """
        return FeedDto.from_camel_case(self.handle_request("DELETE", f"{self._feed_url}/{feed_id}")["data"])
