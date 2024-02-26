"""
This module is used to define the ``SubscriberApi``, a python wrapper to interact with ``Subscribers`` in Novu.
"""

from typing import Dict, Iterator, List, Optional, Union

import requests

from novu.api.base import Api, PaginationIterator
from novu.constants import SUBSCRIBERS_ENDPOINT
from novu.dto.message import MessageDto
from novu.dto.subscriber import (
    BulkResultSubscriberDto,
    PaginatedSubscriberDto,
    SubscriberDto,
    SubscriberPreferenceDto,
)
from novu.enums import Channel, MarkAsEnum, MessageActionStatus, ProviderIdEnum


class SubscriberApi(Api):
    """This class aims to handle all API methods around subscribers in API"""

    def __init__(
        self,
        url: Optional[str] = None,
        api_key: Optional[str] = None,
        requests_timeout: Optional[int] = None,
        session: Optional[requests.Session] = None,
    ) -> None:
        super().__init__(url=url, api_key=api_key, requests_timeout=requests_timeout, session=session)

        self._subscriber_url = f"{self._url}{SUBSCRIBERS_ENDPOINT}"

    def list(self, page: Optional[int] = None) -> PaginatedSubscriberDto:
        """Method to list subscriber

        Args:
            page: The page number. Defaults to 0.

        Returns:
            Paginated subscriber
        """
        payload: Dict[str, int] = {}
        if page:
            payload["page"] = page

        return PaginatedSubscriberDto.from_camel_case(self.handle_request("GET", self._subscriber_url, payload=payload))

    def stream(self) -> PaginationIterator[SubscriberDto]:
        """Stream all existing subscribers into an iterator.

        Returns:
            An iterator on all subscribers available.
        """
        return PaginationIterator(self, SubscriberDto, self._subscriber_url)

    def create(self, subscriber: SubscriberDto) -> SubscriberDto:
        """Method to push a given subscriber instance to Novu

        Args:
            subscriber: The subscriber instance to push to Novu

        Returns:
            The instance retrieved from Novu (populated after creation)
        """
        return SubscriberDto.from_camel_case(
            self.handle_request("POST", self._subscriber_url, subscriber.to_camel_case()).get("data", {})
        )

    def bulk_create(self, subscribers: Iterator[SubscriberDto]) -> BulkResultSubscriberDto:
        """Using this endpoint you can create multiple subscribers at once, to avoid multiple calls to the API.

        The bulk API is limited to 500 subscribers per request.

        Args:
            subscribers: An iterator of subscribers instance to push to Novu

        Returns:
            Result of the bulk operation in Novu.
        """
        return BulkResultSubscriberDto.from_camel_case(
            self.handle_request(
                "POST",
                f"{self._subscriber_url}/bulk",
                {"subscribers": [subscriber.to_camel_case() for subscriber in subscribers]},
            ).get("data", {})
        )

    def get(self, subscriber_id: str) -> SubscriberDto:
        """Method to get a subscriber using his identifier

        Args:
            subscriber_id: The subscriber identifier

        Returns:
            The subscriber instance
        """
        return SubscriberDto.from_camel_case(
            self.handle_request("GET", f"{self._subscriber_url}/{subscriber_id}").get("data", {})
        )

    def put(self, subscriber: SubscriberDto) -> SubscriberDto:
        """Method to update a subscriber using his instance

        Args:
            subscriber: The subscriber instance to push

        Returns:
            Updated subscriber instance from Novu API
        """
        return SubscriberDto.from_camel_case(
            self.handle_request(
                "PUT", f"{self._subscriber_url}/{subscriber.subscriber_id}", subscriber.to_camel_case()
            ).get("data", {})
        )

    def delete(self, subscriber_id: str) -> None:
        """Method used to delete a subscriber using his identifier

        Args:
            subscriber_id: The subscriber identifier
        """
        self.handle_request("DELETE", f"{self._subscriber_url}/{subscriber_id}")

    def credentials(
        self,
        subscriber_id: str,
        provider_id: str,
        webhook_url: Optional[str] = None,
        device_tokens: Optional[List[str]] = None,
    ) -> SubscriberDto:
        """Update subscriber credentials associated to the delivery methods such as slack and push tokens

        Args:
            subscriber_id: The subscriber identifier
            provider_id: The provider name (e.g: slack)
            webhook_url: The webhook URL to set in the provider credentials. Defaults to None.
            device_tokens: A list of device tokens to set in the provider credentials. Defaults to None.

        Returns:
            Updated subscriber
        """
        credentials: Dict[str, Union[str, List[str]]] = {}
        payload = {"providerId": provider_id, "credentials": credentials}

        if webhook_url:
            credentials["webhookUrl"] = webhook_url
        if device_tokens:
            credentials["deviceTokens"] = device_tokens

        return SubscriberDto.from_camel_case(
            self.handle_request("PUT", f"{self._subscriber_url}/{subscriber_id}/credentials", payload).get("data", {})
        )

    def delete_credentials(
        self,
        subscriber_id: str,
        provider_id: ProviderIdEnum,
    ) -> None:
        """Delete subscriber credentials such as slack and expo tokens.

        Args:
            subscriber_id: The subscriber identifier
            provider_id: The provider identifier (e.g: slack)
        """

        self.handle_request("DELETE", f"{self._subscriber_url}/{subscriber_id}/credentials/{provider_id}")

    def online_status(self, subscriber_id: str, status: bool) -> SubscriberDto:
        """Used to update the subscriber is_online flag

        Args:
            subscriber_id: The subscriber identifier.
            status: The subscriber is_online flag value.

        Returns:
            Updated subscriber
        """
        return SubscriberDto.from_camel_case(
            self.handle_request(
                "PATCH", f"{self._subscriber_url}/{subscriber_id}/online-status", {"isOnline": status}
            ).get("data", {})
        )

    def preferences(self, subscriber_id: str) -> Iterator[SubscriberPreferenceDto]:
        """Get the subscriber preferences

        Args:
            subscriber_id: The subscriber identifier

        Yield:
            Iterator of subscriber preference
        """
        results = self.handle_request("GET", f"{self._subscriber_url}/{subscriber_id}/preferences").get("data", [])
        for result in results:
            yield SubscriberPreferenceDto.from_camel_case(result)

    def change_channel_preference(
        self, subscriber_id: str, template_id: str, channel: Channel, channel_enabled: bool
    ) -> SubscriberPreferenceDto:
        """Change the subscriber preference for a targeted channel of given template

        Args:
            subscriber_id: The subscriber on which we want to change preference
            template_id: The template on which we want to change preference
            channel: The channel on which we want to change preference
            channel_enabled: The new state of activation of the channel

        Returns:
            Updated subscriber preference of the targeted template
        """
        return SubscriberPreferenceDto.from_camel_case(
            self.handle_request(
                "PATCH",
                f"{self._subscriber_url}/{subscriber_id}/preferences/{template_id}",
                {"channel": {"type": channel, "enabled": channel_enabled}},
            ).get("data", {})
        )

    def change_preference_state(self, subscriber_id: str, template_id: str, state: bool) -> SubscriberPreferenceDto:
        """Change the subscriber preference state (enabled or disabled) for a given template

        Args:
            subscriber_id: The subscriber identifier
            template_id: The template identifier
            state: The state of the subscriber preference for given template

        Returns:
            Updated subscriber preference of the targeted template
        """
        return SubscriberPreferenceDto.from_camel_case(
            self.handle_request(
                "PATCH", f"{self._subscriber_url}/{subscriber_id}/preferences/{template_id}", {"enabled": state}
            ).get("data", {})
        )

    def unseen_notifications(self, subscriber_id: str) -> int:
        """Retrieve the number of unseen notification for subscribers feed

        Args:
            subscriber_id: The subscriber identifier

        Returns:
            The number of unseen notification
        """
        res = self.handle_request("GET", f"{self._subscriber_url}/{subscriber_id}/notifications/unseen")
        return res.get("data", {}).get("count", 0)

    def mark_as(
        self, subscriber_id: str, message_id: str, seen: Optional[bool] = None, read: Optional[bool] = None
    ) -> MessageDto:
        """Mark a subscriber feed message as seen or read.

        Args:
            subscriber_id: The subscriber identifier
            message_id: The message identifier
            seen: If provided, set the 'seen' state of the message
            read: If provided, set the 'read' state of the message

        Returns:
            Return the updated message
        """
        mark: Dict[str, bool] = {}
        if read is not None:
            mark["read"] = read
        if seen is not None:
            mark["seen"] = seen
        payload = {"messageId": message_id, "mark": mark}

        return MessageDto.from_camel_case(
            self.handle_request("POST", f"{self._subscriber_url}/{subscriber_id}/messages/markAs", json=payload)[
                "data"
            ][0]
        )

    def mark_all_as(self, subscriber_id: str, mark_as: MarkAsEnum, feed_identifiers: Optional[List[str]] = None) -> int:
        """Mark all the subscriber messages as read, unread, seen or unseen.

        Args:
            subscriber_id: The subscriber identifier
            mark_as: Mark all subscriber messages as read, unread, seen or unseen via this instruction
            feed_identifiers: Optionally, you can pass a list of feed identifiers to mark messages of a particular feed.

        Returns:
            Number of updated messages.
        """
        payload: Dict[str, Union[List[str], MarkAsEnum]] = {"markAs": mark_as}
        if feed_identifiers:
            payload["feedIdentifier"] = feed_identifiers

        return self.handle_request(
            "POST", f"{self._subscriber_url}/{subscriber_id}/messages/mark-all", json=payload
        ).get("data", 0)

    def mark_message_action(
        self,
        subscriber_id: str,
        message_id: str,
        action_type: str,
        status: MessageActionStatus,
        payload: Optional[dict] = None,
    ) -> MessageDto:
        """Mark message action as seen.

        Args:
            subscriber_id: The subscriber identifier
            message_id: The message identifier
            action_type: The message action type
            status: The message action status
            payload: The message action payload

        Returns:
            Return the updated message
        """
        body: Dict[str, Union[MessageActionStatus, dict]] = {"status": status}
        if payload is not None:
            body["payload"] = payload

        return MessageDto.from_camel_case(
            self.handle_request(
                "POST", f"{self._subscriber_url}/{subscriber_id}/messages/{message_id}/actions/{action_type}", json=body
            ).get("data", {})
        )
