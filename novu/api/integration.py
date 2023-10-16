"""
This module is used to define the ``IntregrationApi``, a python wrapper to interact with ``Integrations`` in Novu.
"""
from typing import Iterator, Optional

import requests

from novu.api.base import Api
from novu.constants import INTEGRATIONS_ENDPOINT
from novu.dto.integration import IntegrationChannelUsageDto, IntegrationDto
from novu.enums import Channel, ProviderIdEnum


class IntegrationApi(Api):
    """This class aims to handle all API methods around integrations in API"""

    def __init__(
        self,
        url: Optional[str] = None,
        api_key: Optional[str] = None,
        requests_timeout: Optional[int] = None,
        session: Optional[requests.Session] = None,
    ) -> None:
        super().__init__(url=url, api_key=api_key, requests_timeout=requests_timeout, session=session)

        self._integration_url = f"{self._url}{INTEGRATIONS_ENDPOINT}"

    def list(self, only_active: bool = False) -> Iterator[IntegrationDto]:
        """List configured integrations

        Args:
            only_active: Allow to retrieve only active integrations. Defaults to False.

        Yields:
            Instance of integrations
        """
        url = self._integration_url
        if only_active:
            url += "/active"

        results = self.handle_request("GET", url)["data"]
        for result in results:
            yield IntegrationDto.from_camel_case(result)

    def create(self, integration: IntegrationDto, check: bool = True) -> IntegrationDto:
        """Create a provider integration configuration

        Args:
            integration: Integration instance that you want to create.
            check:
                If you want the Novu server to check his connection using given integration configuration.
                Defaults to True.

        Returns:
            The instance of the created integration
        """
        payload = integration.to_camel_case()
        payload["check"] = check if check is not None else True

        return IntegrationDto.from_camel_case(self.handle_request("POST", self._integration_url, payload)["data"])

    def status(self, provider_id: ProviderIdEnum) -> bool:
        """Get webhook support status for a given provider

        Args:
            provider_id: The provider ID

        Returns:
            If the provider support webhook
        """
        return self.handle_request("GET", f"{self._integration_url}/webhooks/provider/{provider_id}/status")["data"]

    def update(self, integration: IntegrationDto, check: bool = True) -> IntegrationDto:
        """Update an integration configuration

        Args:
            integration: The instance of the integration to update
            check:
                If you want the Novu server to check his connection using given integration configuration.
                Defaults to True.

        Returns:
            The instance of the updated integration
        """
        payload = integration.to_camel_case()
        payload["check"] = check if check is not None else True

        return IntegrationDto.from_camel_case(
            self.handle_request("PUT", f"{self._integration_url}/{integration._id}", payload)["data"]
        )

    def delete(self, integration_id: str) -> None:
        """Delete an integration definition

        Args:
            integration_id: The integration ID
        """
        self.handle_request("DELETE", f"{self._integration_url}/{integration_id}")

    def limit(self, channel: Channel) -> IntegrationChannelUsageDto:
        """Get limit of the given channel (and usage)

        Args:
            channel: The channel to retrieve limits

        Returns:
            Channel usage definition (including usage and limit)
        """
        return IntegrationChannelUsageDto.from_camel_case(
            self.handle_request("GET", f"{self._integration_url}/{channel}/limit")["data"]
        )

    def set_primary(self, integration_id: str) -> IntegrationDto:
        """Set an integration as primary
        Args:
            integration_id: The integration ID
        Raises:
            HTTPError: Raise a 400 error when provided integration identifier is not found in the application
            HTTPError: Raise a 401 error when you are not authorized to do this action
        Returns:
            The instance of the updated integration
        """
        return IntegrationDto.from_camel_case(
            self.handle_request("POST", f"{self._integration_url}/{integration_id}/set-primary")["data"]
        )
