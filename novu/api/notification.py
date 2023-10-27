"""This module is used to define the ``NotificationAPI`, a python wrapper
to interact with ``Notifications`` in Novu.
"""
from typing import Iterator, List, Optional, Tuple

import requests

from novu.api.base import Api, PaginationIterator, RetryConfig
from novu.constants import NOTIFICATION_ENDPOINT
from novu.dto.notification import (
    ActivityGraphStatesDto,
    ActivityNotificationDto,
    PaginatedActivityNotificationDto,
)


class NotificationApi(Api):
    """This class aims to handle all API methods around notifications in API"""

    def __init__(
        self,
        url: Optional[str] = None,
        api_key: Optional[str] = None,
        requests_timeout: Optional[int] = None,
        retry_config: Optional[RetryConfig] = None,
        session: Optional[requests.Session] = None,
    ) -> None:
        super().__init__(
            url=url, api_key=api_key, requests_timeout=requests_timeout, retry_config=retry_config, session=session
        )

        self._notification_url = f"{self._url}{NOTIFICATION_ENDPOINT}"

    def list(
        self,
        channels: Optional[List[str]] = None,
        templates: Optional[List[str]] = None,
        emails: Optional[List[str]] = None,
        search: Optional[str] = None,
        page: Optional[int] = 0,
        transaction_id: Optional[str] = None,
    ) -> PaginatedActivityNotificationDto:
        """Trigger an event to get all notifications.

        Args:
            channels: A required parameter, should be an array of strings representing
                           available notification channels, such as "in_app", "email", "sms",
                           "chat", and "push".

            templates: A required parameter, should be an array of strings representing
                             the notification templates.

            emails: A required parameter, should be an array of strings representing
                        the email addresses associated with the notification.

            search: A required parameter, should be a string representing the search query.

            page: An optional parameter with a default value of 0, representing the page
                     number for search results.

            transaction_id: A required parameter, should be a string representing the
                                transaction ID associated with the notification.

        Returns:
            Gets notifications in Novu

        """
        payload = {
            "channels": channels,
            "templates": templates,
            "emails": emails,
            "search": search,
            "page": page,
            "transactionId": transaction_id,
        }
        return PaginatedActivityNotificationDto.from_camel_case(
            self.handle_request("GET", f"{self._notification_url}", payload=payload)
        )

    def stream(
        self,
        channels: Optional[List[str]] = None,
        templates: Optional[List[str]] = None,
        emails: Optional[List[str]] = None,
        search: Optional[str] = None,
        transaction_id: Optional[str] = None,
    ) -> PaginationIterator[ActivityNotificationDto]:
        """Stream all existing notifications into an iterator.

        Args:
            channels: A required parameter, should be an array of strings representing
                           available notification channels, such as "in_app", "email", "sms",
                           "chat", and "push".

            templates: A required parameter, should be an array of strings representing
                             the notification templates.

            emails: A required parameter, should be an array of strings representing
                        the email addresses associated with the notification.

            search: A required parameter, should be a string representing the search query.

            transaction_id: A required parameter, should be a string representing the
                                transaction ID associated with the notification.

        Returns:
            An iterator on all notifications available.
        """
        payload = {
            "channels": channels,
            "templates": templates,
            "emails": emails,
            "search": search,
            "transactionId": transaction_id,
        }
        return PaginationIterator(self, ActivityNotificationDto, self._notification_url, payload=payload)

    def stats(self) -> Tuple[int, int]:
        """Gets notifications stats

        Returns:
            Tuple including weekly and monthly sent notifications.
        """
        data = self.handle_request("GET", f"{self._notification_url}/stats")["data"]
        return data["weeklySent"], data["monthlySent"]

    def graph_stats(
        self,
        id: Optional[str] = None,  # pylint: disable=C0103,W0622
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        days: Optional[int] = None,
    ) -> Iterator[ActivityGraphStatesDto]:
        """Gets notifications graph stats.

        Args:
           id: is an optional parameter and should be a string. It represents the notification ID.
           start_date: is an optional parameter and should be a string. It represents the start date for the stats.
           end_date: is an optional parameter and should be a string. It represents the end date for the stats.
           days: is an optional parameter and should be an integer. It represents the number of days to get stats for.

        Returns:
           An iterator on notifications graph stats in Novu
        """
        payload = {
            "id": id,
            "start_date": start_date,
            "end_date": end_date,
            "days": days,
        }
        response = self.handle_request("GET", f"{self._notification_url}/graph/stats", payload=payload)
        for data in response["data"]:
            yield ActivityGraphStatesDto.from_camel_case(data)

    def get(self, notification_id: str) -> ActivityNotificationDto:
        """Trigger an event to get  notification by id"""
        url = f"{self._notification_url}/{notification_id}"
        response = self.handle_request("GET", url)
        return ActivityNotificationDto.from_camel_case(response["data"])
