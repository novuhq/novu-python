"""
This module is used to define the ``NotificationTemplateApi``, a python wrapper
to interact with ``NotificationTemplate`` in Novu.
"""

from typing import Optional

import requests

from novu.api.base import Api, PaginationIterator
from novu.constants import NOTIFICATION_TEMPLATES_ENDPOINT
from novu.dto.notification_template import (
    NotificationTemplateDto,
    NotificationTemplateFormDto,
    PaginatedNotificationTemplateDto,
)


class NotificationTemplateApi(Api):
    """This class aims to handle all API methods around notification templates in API"""

    def __init__(
        self,
        url: Optional[str] = None,
        api_key: Optional[str] = None,
        requests_timeout: Optional[int] = None,
        session: Optional[requests.Session] = None,
    ) -> None:
        super().__init__(url=url, api_key=api_key, requests_timeout=requests_timeout, session=session)

        self._notification_template_url = f"{self._url}{NOTIFICATION_TEMPLATES_ENDPOINT}"

    def list(self, page: Optional[int] = None, limit: Optional[int] = None) -> PaginatedNotificationTemplateDto:
        """Method to list notification templates

        Returns:
            Paginated notification templates
        """
        payload = {}
        if page is not None:
            payload["page"] = page
        if limit is not None:
            payload["limit"] = limit

        return PaginatedNotificationTemplateDto.from_camel_case(
            self.handle_request("GET", self._notification_template_url, payload=payload)
        )

    def stream(self) -> PaginationIterator[NotificationTemplateDto]:
        """Stream all existing workflows into an iterator.

        Returns:
            An iterator on all workflows available.
        """
        return PaginationIterator(self, NotificationTemplateDto, self._notification_template_url)

    def create(self, notification_template: NotificationTemplateFormDto) -> NotificationTemplateDto:
        """Create a template using the notification template form definition

        Args:
            notification_template: The notification template form definition

        Returns:
            Mapped notification template after it's creation
        """
        return NotificationTemplateDto.from_camel_case(
            self.handle_request("POST", self._notification_template_url, notification_template.to_camel_case())["data"]
        )

    def get(self, notification_template_id: str) -> NotificationTemplateDto:
        """Retrieve a notification template using it's Novu ID

        Args:
            notification_template_id: The Novu ID of the notification template

        Returns:
            Mapped notification template
        """
        return NotificationTemplateDto.from_camel_case(
            self.handle_request("GET", f"{self._notification_template_url}/{notification_template_id}")["data"]
        )

    def update(
        self, notification_template_id: str, notification_template: NotificationTemplateFormDto
    ) -> NotificationTemplateDto:
        """Full update of a notification template, using it's template form definition

        Args:
            notification_template_id: The Novu ID of the notification template
            notification_template: The notification template from instance

        Returns:
            Mapped notification template after it's update
        """
        return NotificationTemplateDto.from_camel_case(
            self.handle_request(
                "PUT",
                f"{self._notification_template_url}/{notification_template_id}",
                notification_template.to_camel_case(),
            )["data"]
        )

    def delete(self, notification_template_id: str) -> None:
        """Delete a notification template using it's ID

        Args:
            notification_template_id: The notification template ID
        """
        self.handle_request("DELETE", f"{self._notification_template_url}/{notification_template_id}")

    def update_status(self, notification_template_id: str, status: bool) -> NotificationTemplateDto:
        """Update a notification template status (active or not) using it's ID and the requested status

        Args:
            notification_template_id: The Novu ID of the notification template
            status: The activation status of the notification template

        Returns:
            Mapped notification template after it's update
        """
        return NotificationTemplateDto.from_camel_case(
            self.handle_request(
                "PUT", f"{self._notification_template_url}/{notification_template_id}/status", {"active": status}
            )["data"]
        )
