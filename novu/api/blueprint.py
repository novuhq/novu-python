"""This module is used to define the ``BlueprintApi``,
a python wrapper to interact with ``Blueprint`` in Novu."""
from typing import Optional

import requests

from novu.api.base import Api
from novu.constants import BLUEPRINTS_ENDPOINT
from novu.dto.blueprint import BlueprintDto, GroupedBlueprintDto


class BlueprintApi(Api):
    """This class aims to handle all API methods around blueprints in Novu"""

    def __init__(
        self,
        url: Optional[str] = None,
        api_key: Optional[str] = None,
        requests_timeout: Optional[int] = None,
        session: Optional[requests.Session] = None,
    ) -> None:
        super().__init__(url=url, api_key=api_key, requests_timeout=requests_timeout, session=session)

        self._blueprint_url = f"{self._url}{BLUEPRINTS_ENDPOINT}"

    def get_by_id(self, template_id: str) -> BlueprintDto:
        """Get a blueprint by ID

        Args:
            template_id: The ID of the blueprint

        Returns:
            The blueprint instance
        """
        return BlueprintDto.from_camel_case(self.handle_request("GET", f"{self._blueprint_url}/{template_id}")["data"])

    def get_grouped_by_category(self) -> GroupedBlueprintDto:
        """Get blueprints grouped by category

        Returns:
            Grouped blueprints instance
        """
        return GroupedBlueprintDto.from_camel_case(
            self.handle_request("GET", f"{self._blueprint_url}/group-by-category")["data"]
        )
