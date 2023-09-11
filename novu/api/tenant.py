"""
This module is used to define the ``TenantApi``, a python wrapper to interact with ``Tenants`` in Novu.
"""
from typing import Dict, Optional, Union

import requests

from novu.api.base import Api
from novu.constants import TENANTS_ENDPOINT
from novu.dto.tenant import PaginatedTenantDto, TenantDto


class TenantApi(Api):
    """This class aims to handle all API methods around tenants in API"""

    def __init__(
        self,
        url: Optional[str] = None,
        api_key: Optional[str] = None,
        requests_timeout: Optional[int] = None,
        session: Optional[requests.Session] = None,
    ) -> None:
        super().__init__(url=url, api_key=api_key, requests_timeout=requests_timeout, session=session)

        self._tenant_url = f"{self._url}{TENANTS_ENDPOINT}"

    def list(self, page: Optional[int] = None, limit: Optional[int] = None) -> PaginatedTenantDto:
        """List existing tenants

        Args:
            page: Page to retrieve. Defaults to None.
            limit: Size of the page to retrieve. Defaults to None.

        Returns:
            Paginated list of tenant
        """
        payload: Dict[str, Union[int, str]] = {}
        if page:
            payload["page"] = page
        if limit:
            payload["limit"] = limit

        return PaginatedTenantDto.from_camel_case(self.handle_request("GET", self._tenant_url, payload=payload))

    def create(self, identifier: str, name: str, data: Optional[dict] = None) -> TenantDto:
        """Create a tenant

        Args:
            identifier: Identifier of the new tenant
            name: Name of the new tenant
            data: Data of the new tenant. Default to None.

        Returns:
            Created tenant
        """
        return TenantDto.from_camel_case(
            self.handle_request("POST", self._tenant_url, {"identifier": identifier, "name": name, "data": data or {}})[
                "data"
            ]
        )

    def get(self, identifier: str) -> TenantDto:
        """Retrieve a Tenant using his identifier

        .. note:: This method is the easiest way to get the list of subscribers.

        Args:
            identifier: The tenant identifier (ID in Novu)

        Returns:
            TenantDto
        """
        return TenantDto.from_camel_case(self.handle_request("GET", f"{self._tenant_url}/{identifier}")["data"])

    def patch(
        self, reference: str, identifier: Optional[str] = None, name: Optional[str] = None, data: Optional[dict] = None
    ) -> TenantDto:
        """Edit a Tenant using his identifier

        Args:
            reference: Current identifier of the tenant in Novu
            identifier: New identifier to set on the tenant
            name: New name to set on the tenant
            data: New data dict to set on the tenant

        Returns:
            TenantDto
        """
        payload = {"identifier": identifier, "name": name, "data": data}
        payload = {k: v for k, v in payload.items() if v}
        return TenantDto.from_camel_case(
            self.handle_request("PATCH", f"{self._tenant_url}/{reference}", payload)["data"]
        )

    def delete(self, identifier: str) -> None:
        """Remove a Tenant using his identifier

        Args:
            identifier: Current identifier of the tenant in Novu
        """
        self.handle_request("DELETE", f"{self._tenant_url}/{identifier}")
