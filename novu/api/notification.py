"""This module is used to define the ``NotificationAPI`, a python wrapper
to interact with ``Notifications`` in Novu.
"""
from typing import Optional

import requests

from novu.api.base import Api
from novu.constants import NOTIFICATION_ENDPOINT
from novu.dto.notification import NotificationDto


class NotificationApi(Api):
    """This class aims to handle all API methods around notifications in API"""

    def __init__(
        self,
        url: Optional[str] = None,
        api_key: Optional[str] = None,
        requests_timeout: Optional[int] = None,
        session: Optional[requests.Session] = None,
    ) -> None:
        super().__init__(url=url, api_key=api_key, requests_timeout=requests_timeout, session=session)

        self._notification_url = f"{self._url}{NOTIFICATION_ENDPOINT}"

    def notification(
        self,
        channels: list[str],
        templates: list[str],
        emails: list[str],
        search: str,
        page: Optional[int] = 0,
        transaction_id: Optional[str] = None,
    ) -> NotificationDto:
        """Trigger an event to get  notifications
        Args:
           channels: is a required parameter and should be an array of strings. It represents the available notification channels, such as "in_app", "email", "sms", "chat", and "push".
           templates: is a required parameter and should be an array of strings. It represents the notification templates.
           emails is a required parameter and should be an array of strings. It represents the email addresses associated with the notification.
           search is a required parameter and should be a string. It represents the search query.
           page is an optional parameter with a default value of 0. It represents the page number for search results.
           transactionId is a required parameter and should be a string. It represents the transaction ID associated with the notification.


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
        return NotificationDto.from_camel_case(
            self.handle_request("GET", f"{self._notification_url}", payload=payload)["data"]
        )

    def notifications_stats(
        self,
        id: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ):
        """Gets notifications stats
        Args:
            id: is an optional parameter and should be a string. It represents the notification ID.
            start_date: is an optional parameter and should be a string. It represents the start date for the stats.
            end_date: is an optional parameter and should be a string. It represents the end date for the stats.


        Returns:
            Gets notifications stats in Novu

        """
        payload = {
            "id": id,
            "start_date": start_date,
            "end_date": end_date,
        }
        response = self.handle_request("GET", f"{self._notification_url}/stats", payload=payload)
        return response

    def notifications_graph_stats(
        self,
        id: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        days: Optional[int] = None,
    ):
        """Gets notifications graph stats
        Args:
           id: is an optional parameter and should be a string. It represents the notification ID.
           start_date: is an optional parameter and should be a string. It represents the start date for the stats.
           end_date: is an optional parameter and should be a string. It represents the end date for the stats.
           days: is an optional parameter and should be an integer. It represents the number of days to get stats for.


        Returns:
           Gets notifications graph stats in Novu

        """
        payload = {
            "id": id,
            "start_date": start_date,
            "end_date": end_date,
            "days": days,
        }
        response = self.handle_request("GET", f"{self._notification_url}/graph/stats", payload=payload)
        return response["data"]

    def check_notification_by_id(self, notification_id: str) -> NotificationDto:
        """Trigger an event to get  notification by id"""
        url = f"{self._notification_url}/{notification_id}"
        response = self.handle_request("GET", url)
        return NotificationDto.from_camel_case(response["data"])
