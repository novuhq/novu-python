"""
This module is used to define the ``EventApi``, a python wrapper to interact with ``Events`` in Novu.
"""
from collections.abc import Iterable
from typing import Iterable as _Iterable, List, Optional, Union

from novu.api.base import Api
from novu.constants import EVENTS_ENDPOINT
from novu.dto.event import EventDto
from novu.dto.topic import TriggerTopicDto


class EventApi(Api):
    """This class aims to handle all API methods around events in Novu"""

    def __init__(self, url: Optional[str] = None, api_key: Optional[str] = None) -> None:
        super().__init__(url, api_key)

        self._event_url = f"{self._url}{EVENTS_ENDPOINT}"

    def trigger(
        self,
        name: str,
        recipients: Union[str, List[str]],
        payload: dict,
        overrides: Optional[dict] = None,
        transaction_id: Optional[str] = None,
        actor: Optional[str] = None,
    ) -> EventDto:
        """Trigger event is the main way to send notification to subscribers.

        The trigger ID is used to match the particular template associated whit it.

        .. note:: If you want to use topic, please use
                  :meth:`~novu.api.event.EventApi.trigger_topic` instead

        .. warning:: For the "recipients" attribute, the part allowing the dynamic creation of
                     subscribers in the Novu AP was deliberately removed from the wrapper
                     to force you to pre-create them. It is for us a good practice that we must
                     begin to use for long-term programming with the platform (reuse of actor
                     during the sending, subscription, management of preferences ...).

        Args:
            name: The name of the template trigger to activate.
            recipients: A subscriber ID (or a list of subscriber ID) to reach with this trigger
            payload:
                A JSON serializable python dict to pass additional custom information that could be used to render the
                template, or perform routing rules based on it. This data will also be available when fetching the
                notifications feed from the API to display certain parts of the UI.

            overrides:
                A JSON serializable python dict used to override provider specific configurations. Defaults to None.

            transaction_id: A unique ID for this transaction, we will generated a UUID if not provided.

            actor:
                It is used to display the Avatar of the provided actor's subscriber id. Defaults to None.

        Returns:
            Create Event definition in Novu
        """
        payload = {"name": name, "to": recipients, "payload": payload}
        if overrides:
            payload["overrides"] = overrides
        if actor:
            payload["actor"] = actor
        if transaction_id:
            payload["transactionId"] = transaction_id

        return EventDto.from_camel_case(self.handle_request("POST", self._event_url, payload)["data"])

    def trigger_topic(
        self,
        name: str,
        topics: Union[TriggerTopicDto, _Iterable[TriggerTopicDto]],
        payload: dict,
        overrides: Optional[dict] = None,
        transaction_id: Optional[str] = None,
        actor: Optional[str] = None,
    ) -> EventDto:
        """Trigger event is the main way to send notification to topic's subscribers.

        The trigger ID is used to match the particular template associated whit it.

        .. note:: If you want to use subscriber ID, please use :meth:`~novu.api.event.EventApi.trigger` instead

        Args:
            name: The name of the template trigger to activate.
            topics: A TriggerTopicDto (or a list of topic) to reach with this trigger
            payload:
                A JSON serializable python dict to pass additional custom information that could be used to render the
                template, or perform routing rules based on it. This data will also be available when fetching the
                notifications feed from the API to display certain parts of the UI.

            overrides:
                A JSON serializable python dict used to override provider specific configurations. Defaults to None.

            transaction_id: A unique ID for this transaction, we will generated a UUID if not provided.

            actor:
                It is used to display the Avatar of the provided actor's subscriber id. Defaults to None.

        Returns:
            Create Event definition in Novu
        """
        _recipients = topics if isinstance(topics, Iterable) else [topics]

        payload = {"name": name, "to": [r.to_camel_case() for r in _recipients], "payload": payload}
        if overrides:
            payload["overrides"] = overrides
        if actor:
            payload["actor"] = actor
        if transaction_id:
            payload["transactionId"] = transaction_id

        return EventDto.from_camel_case(self.handle_request("POST", self._event_url, payload)["data"])

    def broadcast(
        self,
        name: str,
        payload: dict,
        overrides: Optional[dict] = None,
        transaction_id: Optional[str] = None,
        actor: Optional[str] = None,
    ):
        """Trigger a broadcast event to all existing subscribers, could be used to send announcements, etc.

        Args:
            name: The name of the template trigger to activate.
            payload:
                A JSON serializable python dict to pass additional custom information that could be used to render the
                template, or perform routing rules based on it. This data will also be available when fetching the
                notifications feed from the API to display certain parts of the UI.

            overrides:
                A JSON serializable python dict used to override provider specific configurations. Defaults to None.

            transaction_id: A unique ID for this transaction, we will generated a UUID if not provided.

            actor:
                It is used to display the Avatar of the provided actor's subscriber id. Defaults to None.

        Returns:
            Create Event definition in Novu
        """
        payload = {"name": name, "payload": payload}
        if overrides:
            payload["overrides"] = overrides
        if actor:
            payload["actor"] = actor
        if transaction_id:
            payload["transactionId"] = transaction_id

        return EventDto.from_camel_case(self.handle_request("POST", f"{self._event_url}/broadcast", payload)["data"])

    def delete(self, transaction_id: str):
        """Using a previously generated transaction ID during the event trigger, will cancel any active or pending
        workflows. This is useful to cancel active digests, delays, etc...

        Args:
            transaction_id: The transaction ID to cancel workflows
        """
        self.handle_request("DELETE", f"{self._event_url}/{transaction_id}")
