"""
This module is used to define the ``OrganizationApi``, a python wrapper to interact with ``Organizations`` in Novu.
"""

from typing import Iterator, Optional

import requests

from novu.api.base import Api
from novu.constants import ORGANIZATION_ENDPOINT
from novu.dto.member import MemberDto
from novu.dto.organization import OrganizationBrandingDto, OrganizationDto


class OrganizationApi(Api):
    """This class aims to handle all API methods around organization in API"""

    def __init__(
        self,
        url: Optional[str] = None,
        api_key: Optional[str] = None,
        requests_timeout: Optional[int] = None,
        session: Optional[requests.Session] = None,
    ) -> None:
        super().__init__(url=url, api_key=api_key, requests_timeout=requests_timeout, session=session)

        self._organization_url = f"{self._url}{ORGANIZATION_ENDPOINT}"

    def list(self) -> Iterator[OrganizationDto]:
        """Fetch all organizations

        Returns:
            Iterator on organizations
        """
        results = self.handle_request("GET", self._organization_url)["data"]
        for result in results:
            yield OrganizationDto.from_camel_case(result)

    def create(self, name: str, logo: Optional[str] = None) -> OrganizationDto:
        """Create a organization and return his instance

        Args:
            organization: The instance of the organization to create

        Returns:
            The created organization instance
        """
        payload = {"name": name}
        if logo:
            payload["logo"] = logo

        return OrganizationDto.from_camel_case(self.handle_request("POST", self._organization_url, payload)["data"])

    def current(self) -> OrganizationDto:
        """Fetch current organization details

        Returns:
            The current organization instance
        """
        return OrganizationDto.from_camel_case(self.handle_request("GET", f"{self._organization_url}/me")["data"])

    def rename(self, name: str) -> None:
        """Rename the organization

        Args:
            name: The new name of the currently selected organization
        """
        self.handle_request("PATCH", self._organization_url, {"name": name})

    def list_members(self) -> Iterator[MemberDto]:
        """Fetch all members of current organizations

        Returns:
            Iterator on members instances
        """
        results = self.handle_request("GET", f"{self._organization_url}/members")["data"]
        for result in results:
            yield MemberDto.from_camel_case(result)

    def remove_member(self, member_id: str) -> MemberDto:
        """Remove a member from the current organization

        Args:
            member_id: The ID of the member to remove

        Returns:
            Instance of the deleted member
        """
        return MemberDto.from_camel_case(
            self.handle_request("DELETE", f"{self._organization_url}/members/{member_id}")["data"]
        )

    def update_branding(self, branding: OrganizationBrandingDto) -> OrganizationBrandingDto:
        """Update branding information for the current organization

        Args:
            branding: Branding instance including all information required to update branding

        Returns:
            The instance of the updated branding information
        """
        return OrganizationBrandingDto.from_camel_case(
            self.handle_request("PUT", f"{self._organization_url}/branding", json=branding.to_camel_case())["data"]
        )
