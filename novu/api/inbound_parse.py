"""
This module is used to define the ``InboundParseApi``, a python wrapper to interact with ``InboundParse`` in Novu.
"""
from typing import Optional

import requests

from novu.api.base import Api
from novu.constants import INBOUND_PARSE_ENDPOINT


class InboundParseApi(Api):
    """This class aims to handle all API methods around inbound-parse functionality in API"""

    def __init__(
        self,
        url: Optional[str] = None,
        api_key: Optional[str] = None,
        requests_timeout: Optional[int] = None,
        session: Optional[requests.Session] = None,
    ) -> None:
        super().__init__(url=url, api_key=api_key, requests_timeout=requests_timeout, session=session)

        self._inbound_parse_url = f"{self._url}{INBOUND_PARSE_ENDPOINT}"

    def validate_mx_record_setup(self) -> bool:
        """Validate the mx record setup for the inbound parse functionality

        Returns:
            If the mx record setup is well setup or not.
        """
        return (
            self.handle_request("GET", f"{self._inbound_parse_url}/mx/status")
            .get("data", {})
            .get("mxRecordConfigured", False)
        )
