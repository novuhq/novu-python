"""
This module is used to define the ``MessageApi``, a python wrapper to interact with ``Messages`` in Novu.
"""

from typing import Dict, Optional, Union

import requests

from novu.api.base import Api, PaginationIterator
from novu.constants import MESSAGES_ENDPOINT
from novu.dto.message import MessageDto, PaginatedMessageDto


class MessageApi(Api):
    """This class aims to handle all API methods around messages in Novu"""

    def __init__(
        self,
        url: Optional[str] = None,
        api_key: Optional[str] = None,
        requests_timeout: Optional[int] = None,
        session: Optional[requests.Session] = None,
    ) -> None:
        super().__init__(url=url, api_key=api_key, requests_timeout=requests_timeout, session=session)

        self._message_url = f"{self._url}{MESSAGES_ENDPOINT}"

    def list(
        self,
        limit: int = 10,
        page: int = 0,
        channel: Optional[str] = None,
        subscriber_id: Optional[str] = None,
        transaction_id: Optional[str] = None,
    ) -> PaginatedMessageDto:
        """List messages

        Args:
            limit: The number of messages to fetch, defaults to 10
            page: The page to fetch, defaults to 0
            channel: The channel for the messages you wish to list. Defaults to None.
            subscriber_id: The subscriberId for the subscriber you like to list messages for
            transaction_id: The transactionId for the messages you wish to list. Defaults to None.

        Returns:
            Returned a paginated struct containing retrieved messages
        """
        payload: Dict[str, Union[str, int]] = {"limit": limit, "page": page}

        if channel:
            payload["channel"] = channel
        if subscriber_id:
            payload["subscriberId"] = subscriber_id
        if transaction_id:
            payload["transactionId"] = transaction_id

        return PaginatedMessageDto.from_camel_case(self.handle_request("GET", self._message_url, payload=payload))

    def stream(
        self, channel: Optional[str] = None, subscriber_id: Optional[str] = None
    ) -> PaginationIterator[MessageDto]:
        """Stream all existing messages into an iterator.

        Args:
            channel: The channel for the messages you wish to list. Defaults to None.
            subscriber_id: The subscriberId for the subscriber you like to list messages for

        Returns:
            An iterator on all messages available.
        """
        payload = {}

        if channel:
            payload["channel"] = channel
        if subscriber_id:
            payload["subscriberId"] = subscriber_id

        return PaginationIterator(self, MessageDto, self._message_url, payload=payload)

    def delete(self, message_id: str) -> bool:
        """Deletes a message entity from the Novu platform

        Args:
            message_id: The message ID to delete

        Returns:
            This function answer if the delete is a success by parsing the acknowledged field in response.
        """
        return self.handle_request("DELETE", f"{self._message_url}/{message_id}")["data"].get("acknowledged", False)
