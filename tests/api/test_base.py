from unittest import TestCase, mock

from requests.exceptions import HTTPError

from novu.api.base import Api
from novu.config import NovuConfig
from tests.factories import MockResponse


class ApiTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        NovuConfig.configure("sample.novu.com", "api-key")
        cls.api = Api()

    @mock.patch("requests.request")
    def test_handle_request_with_header_override(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, {})

        res = self.api.handle_request("GET", self.api._url, headers={"MyHeader": "value"})
        self.assertEqual(res, {})

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com",
            headers={"Authorization": "ApiKey api-key", "MyHeader": "value"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_handle_request_raise_with_details(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(500, {"details": "my-detail"})

        self.assertRaises(
            HTTPError, lambda: self.api.handle_request("GET", self.api._url, headers={"MyHeader": "value"})
        )

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com",
            headers={"Authorization": "ApiKey api-key", "MyHeader": "value"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_handle_request_raise_without_details(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(500, raise_on_json_decode=True)

        self.assertRaises(
            HTTPError, lambda: self.api.handle_request("GET", self.api._url, headers={"MyHeader": "value"})
        )

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com",
            headers={"Authorization": "ApiKey api-key", "MyHeader": "value"},
            json=None,
            params=None,
            timeout=5,
        )
