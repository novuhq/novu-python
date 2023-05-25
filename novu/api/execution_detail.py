"""
This module is used to define the ``ExecutionDetailApi``, a python wrapper
to interact with ``ExecutionDetails`` in Novu.
"""
from typing import Iterator, Optional

from novu.api.base import Api
from novu.constants import EXECUTION_DETAILS_ENDPOINT
from novu.dto import ExecutionDetailDto


class ExecutionDetailApi(Api):
    """This class aims to handle all API methods around execution details in Novu"""

    def __init__(
        self, url: Optional[str] = None, api_key: Optional[str] = None, requests_timeout: Optional[int] = None
    ) -> None:
        super().__init__(url, api_key, requests_timeout)

        self._execution_detail_url = f"{self._url}{EXECUTION_DETAILS_ENDPOINT}"

    def list(self, notification_id: str, subscriber_id: str) -> Iterator[ExecutionDetailDto]:
        """List existing execution details using provided notification and subscriber IDs

        Args:
            notification_id: The notification ID in Novu
            subscriber_id: The subscriber ID in Novu

        Yields:
            Mapped execution detail
        """
        results = self.handle_request(
            "GET",
            self._execution_detail_url,
            payload={"notificationId": notification_id, "subscriberId": subscriber_id},
        )["data"]
        for result in results:
            yield ExecutionDetailDto.from_camel_case(result)
