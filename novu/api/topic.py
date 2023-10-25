"""
This module is used to define the ``TopicApi``, a python wrapper to interact with ``Topics`` in Novu.
"""
from typing import Dict, List, Optional, Tuple, Union

import requests

from novu.api.base import Api
from novu.constants import TOPICS_ENDPOINT
from novu.dto.topic import PaginatedTopicDto, TopicDto


class TopicApi(Api):
    """This class aims to handle all API methods around topics in API"""

    def __init__(
        self,
        url: Optional[str] = None,
        api_key: Optional[str] = None,
        requests_timeout: Optional[int] = None,
        session: Optional[requests.Session] = None,
    ) -> None:
        super().__init__(url=url, api_key=api_key, requests_timeout=requests_timeout, session=session)

        self._topic_url = f"{self._url}{TOPICS_ENDPOINT}"

    def list(
        self, page: Optional[int] = None, limit: Optional[int] = None, key: Optional[str] = None
    ) -> PaginatedTopicDto:
        """List existing topics

        Args:
            page: Page to retrieve. Defaults to None.
            limit: Size of the page to retrieve. Defaults to None.
            key: Filter list by a topic key. Defaults to None.

        Returns:
            Paginated list of topic
        """
        payload: Dict[str, Union[int, str]] = {}
        if page:
            payload["page"] = page
        if limit:
            payload["limit"] = limit
        if key:
            payload["key"] = key

        return PaginatedTopicDto.from_camel_case(self.handle_request("GET", self._topic_url, payload=payload))

    def create(self, key: str, name: str) -> TopicDto:
        """Create a topic

        Args:
            key: The topic key to create
            name: The topic name to create

        Returns:
            Created topic (without name ?)
        """
        return TopicDto.from_camel_case(
            self.handle_request("POST", self._topic_url, TopicDto(key, name).to_camel_case())["data"]
        )

    def get(self, key: str) -> TopicDto:
        """Retrieve a Topic using his key

        .. note:: This method is the easiest way to get the list of subscribers.

        Args:
            key: The topic key (ID in Novu)

        Returns:
            Topic
        """
        return TopicDto.from_camel_case(self.handle_request("GET", f"{self._topic_url}/{key}")["data"])

    # FIXME: In documentation, doesn't return anything. But in real life ?
    def subscribe(self, key: str, subscribers: Union[List[str], str]) -> Tuple[List[str], Dict[str, List[str]]]:
        """Subscribe a list of subscribers to a topic

        Args:
            key: The key of the topic to subscribe
            subscribers: The list of subscribers to subscribe

        Returns:
            First element returned is a list of succeeded subscriptions.

            Second element returned is a dict of failed subscriptions
            (key the reason and value contains a list of reference which fail for the reason).
        """
        payload = {"subscribers": subscribers if isinstance(subscribers, list) else [subscribers]}
        result = self.handle_request("POST", f"{self._topic_url}/{key}/subscribers", payload)
        return result["data"].get("succeeded", []), result["data"].get("failed", {})

    def unsubscribe(self, key: str, subscribers: Union[List[str], str]) -> None:
        """Unsubscribe a list of subscribers form a topic

        Args:
            key: The key of the topic to unsubscribe
            subscribers: The list of subscribers to unsubscribe
        """
        payload = {"subscribers": subscribers if isinstance(subscribers, list) else [subscribers]}
        self.handle_request("POST", f"{self._topic_url}/{key}/subscribers/removal", payload)

    def rename(self, key: str, name: str) -> TopicDto:
        """Rename a topic

        Args:
            key: The key of the topic to rename
            name: The new name of the topic

        Returns:
            Renamed topic definition
        """
        return TopicDto.from_camel_case(
            self.handle_request("PATCH", f"{self._topic_url}/{key}", {"name": name})["data"]
        )

    def delete(self, key: str) -> None:
        """Delete a topic by its topic key if it has no subscribers

        Args:
            Key: The topic key to delete
        """

        self.handle_request("DELETE", f"{self._topic_url}/{key}")
