"""
This module is used to define the ``LayoutApi``, a python wrapper to interact with ``Layouts`` in Novu.
"""
from typing import Optional

import requests

from novu.api.base import Api, RetryConfig
from novu.constants import LAYOUTS_ENDPOINT
from novu.dto.layout import LayoutDto, PaginatedLayoutDto


class LayoutApi(Api):
    """This class aims to handle all API methods around layout in API"""

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

        self._layout_url = f"{self._url}{LAYOUTS_ENDPOINT}"

    def list(self, page: Optional[int] = None, limit: Optional[int] = None) -> PaginatedLayoutDto:
        """List existing layouts

        Args:
            page: Page in pagination. Defaults to None.
            limit: Size of the page in pagination. Defaults to None.

        Returns:
            Paginated list of layout
        """
        payload = {"page": page if page is not None else 0, "pageSize": limit if limit is not None else 100}

        return PaginatedLayoutDto.from_camel_case(self.handle_request("GET", self._layout_url, payload=payload))

    def create(self, layout: LayoutDto) -> LayoutDto:
        """Create a layout and return his identifier

        Args:
            layout: The instance of the layout to create

        Returns:
            The created layout identifier
        """
        return LayoutDto.from_camel_case(self.handle_request("POST", self._layout_url, layout.to_camel_case())["data"])

    def get(self, layout_id: str) -> LayoutDto:
        """Get a layout using ID

        Args:
            layout_id: The layout ID

        Returns:
            The layout instance
        """
        return LayoutDto.from_camel_case(self.handle_request("GET", f"{self._layout_url}/{layout_id}")["data"])

    def patch(self, layout: LayoutDto) -> LayoutDto:
        """Update a layout

        Args:
            layout: The instance of the layout to patch

        Returns:
            Updated layout instance
        """
        return LayoutDto.from_camel_case(
            self.handle_request("PATCH", f"{self._layout_url}/{layout._id}", layout.to_camel_case())["data"]
        )

    def delete(self, layout_id: str) -> None:
        """Remove a layout

        Args:
            layout_id: The ID of the layout to remove
        """
        self.handle_request("DELETE", f"{self._layout_url}/{layout_id}")

    def set_default(self, layout_id: str) -> None:
        """Set a layout as the default layout to use

        Args:
            layout_id: The layout ID
        """
        self.handle_request("POST", f"{self._layout_url}/{layout_id}/default")
