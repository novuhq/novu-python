"""
This module is used to define the ``ChangeApi``, a python wrapper to interact with ``Changes`` in Novu.
"""
from typing import Dict, Generator, List, Optional, Union

from novu.api.base import Api
from novu.constants import CHANGES_ENDPOINT
from novu.dto.change import ChangeDto, PaginatedChangeDto


class ChangeApi(Api):
    """This class aims to handle all API methods around changes in API"""

    def __init__(
        self, url: Optional[str] = None, api_key: Optional[str] = None, requests_timeout: Optional[int] = None
    ) -> None:
        super().__init__(url, api_key, requests_timeout)

        self._change_url = f"{self._url}{CHANGES_ENDPOINT}"

    def list(self, page: Optional[int] = None, limit: Optional[int] = None) -> PaginatedChangeDto:
        """List existing changes

        Args:
            page: Page to retrieve. Defaults to None.
            limit: Size of the page to retrieve. Defaults to None.

        Returns:
            Paginated list of change
        """
        payload: Dict[str, Union[int, str]] = {}
        if page:
            payload["page"] = page
        if limit:
            payload["limit"] = limit

        return PaginatedChangeDto.from_camel_case(self.handle_request("GET", self._change_url, payload=payload))

    def count(self) -> int:
        """Get the number of changes

        Returns:
            Number of changes
        """
        return self.handle_request("GET", f"{self._change_url}/count")["data"]

    def apply(self, change_id: str) -> PaginatedChangeDto:
        """Apply one change using its ID

        Args:
            change_ids: A change ID to apply.

        Returns:
            Paginated changes
        """
        return PaginatedChangeDto.from_camel_case(self.handle_request("POST", f"{self._change_url}/{change_id}/apply"))

    def bulk_apply(self, change_ids: List[str]) -> Generator[ChangeDto, None, None]:
        """Apply a list of changes using their IDs

        Args:
            change_ids: The list of IDs to apply

        Yields:
            Parsed Change from results list
        """
        results = self.handle_request("POST", f"{self._change_url}/bulk/apply", {"changeIds": change_ids})["data"]
        for result in results:
            for sub_result in result:
                yield ChangeDto.from_camel_case(sub_result)
