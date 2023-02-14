"""
This module is used to define the ``EnvironmentApi``, a python wrapper to interact with ``Environments`` in Novu.
"""
from typing import Dict, Iterator, Optional

from novu.api.base import Api
from novu.constants import ENVIRONMENTS_ENDPOINT
from novu.dto import EnvironmentApiKeyDto, EnvironmentDto


class EnvironmentApi(Api):
    """This class aims to handle all API methods around environments in Novu"""

    def __init__(self, url: Optional[str] = None, api_key: Optional[str] = None) -> None:
        super().__init__(url, api_key)

        self._environment_url = f"{self._url}{ENVIRONMENTS_ENDPOINT}"

    def list(self) -> Iterator[EnvironmentDto]:
        """List existing environments

        Yields:
            Mapped environment
        """
        results = self.handle_request("GET", self._environment_url)["data"]
        for result in results:
            yield EnvironmentDto.from_camel_case(result)

    def create(self, name: str, parent_id: Optional[str] = None) -> EnvironmentDto:
        """Create a new environment using it's name

        Args:
            name: The name of the environment to create
            parent_id: The parent of the environment to create. Default to None.

        Returns:
            Mapped created environment
        """
        body: Dict[str, str] = {"name": name}
        if parent_id:
            body["parentId"] = parent_id

        return EnvironmentDto.from_camel_case(self.handle_request("POST", self._environment_url, body)["data"])

    def current(self) -> EnvironmentDto:
        """Retrieve the current environment

        Returns:
            Current environment mapped to DTO
        """
        return EnvironmentDto.from_camel_case(self.handle_request("GET", f"{self._environment_url}/me")["data"])

    def api_keys(self) -> Iterator[EnvironmentApiKeyDto]:
        """Remove a environment using it's identifier

        Yields:
            Mapped environment's api keys
        """
        results = self.handle_request("GET", f"{self._environment_url}/api-keys")["data"]
        for result in results:
            yield EnvironmentApiKeyDto.from_camel_case(result)
