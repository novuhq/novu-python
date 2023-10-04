"""
This module is used to define the ``NotificationGroupApi``, a python wrapper
to interact with ``NotificationGroup`` in Novu.
"""
from typing import Optional

import requests

from novu.api.base import Api
from novu.constants import NOTIFICATION_GROUPS_ENDPOINT
from novu.dto.notification_group import (
    NotificationGroupDto,
    PaginatedNotificationGroupDto,
)


class NotificationGroupApi(Api):
    """This class aims to handle all API methods around notification groups in API"""

    def __init__(
        self,
        url: Optional[str] = None,
        api_key: Optional[str] = None,
        requests_timeout: Optional[int] = None,
        session: Optional[requests.Session] = None,
    ) -> None:
        super().__init__(url=url, api_key=api_key, requests_timeout=requests_timeout, session=session)

        self._notification_group_url = f"{self._url}{NOTIFICATION_GROUPS_ENDPOINT}"

    def list(self) -> PaginatedNotificationGroupDto:
        """Method to list notification groups

        Returns:
            Paginated notification groups
        """
        return PaginatedNotificationGroupDto.from_camel_case(self.handle_request("GET", self._notification_group_url))

    def create(self, name: str) -> NotificationGroupDto:
        """Method to create a new notification group

        Args:
            name: The name of the notification group.

        Returns:
            The created notification group.
        """
        return NotificationGroupDto.from_camel_case(
            self.handle_request("POST", self._notification_group_url, {"name": name})["data"]
        )

    def get(self, _id: str) -> NotificationGroupDto:
        """Method to get a notification group

        Args:
            _id: The id of the notification group.

        Returns:
            The notification group.
        """
        return NotificationGroupDto.from_camel_case(
            self.handle_request("GET", f"{self._notification_group_url}/{_id}")["data"]
        )

    def patch(self, _id: str, name: str) -> NotificationGroupDto:
        """Method to patch a notification group

        Args:
            _id: The id of the notification group.
            name: The name of the notification group.

        Returns:
            The patched notification group.
        """
        return NotificationGroupDto.from_camel_case(
            self.handle_request("PATCH", f"{self._notification_group_url}/{_id}", {"name": name})["data"]
        )

    def delete(self, _id: str) -> NotificationGroupDto:
        """Method to delete a notification group

        Args:
            _id: The id of the notification group.

        Returns:
            The deleted notification group.
        """
        return self.handle_request("DELETE", f"{self._notification_group_url}/{_id}")["data"]
