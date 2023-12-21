import copy
from unittest import TestCase, mock

import pkg_resources

from novu.api import TenantApi
from novu.api.base import PaginationIterator
from novu.config import NovuConfig
from novu.dto.tenant import PaginatedTenantDto, TenantDto
from tests.factories import MockResponse

__version__ = pkg_resources.get_distribution("novu").version


class TenantApiTests(TestCase):
    api: TenantApi

    tenant_json = {
        "_id": "63e17e5b33a4f299199329b5",
        "_environmentId": "63dafed97779f59258e38445",
        "identifier": "my-tenant",
        "name": "My Tenant",
        "data": {},
    }
    response_list = {"page": 0, "hasMore": False, "pageSize": 10, "data": [tenant_json]}
    response_get = {"data": tenant_json}
    expected_dto = TenantDto(
        _id="63e17e5b33a4f299199329b5",
        _environment_id="63dafed97779f59258e38445",
        identifier="my-tenant",
        name="My Tenant",
        data={},
    )

    @classmethod
    def setUpClass(cls) -> None:
        NovuConfig.configure("sample.novu.com", "api-key")
        cls.api = TenantApi()

    @mock.patch("requests.request")
    def test_list_tenant(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_list)

        result = self.api.list()
        self.assertIsInstance(result, PaginatedTenantDto)
        self.assertEqual(list(result.data), [self.expected_dto])  # type: ignore

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/tenants",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params={},
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_list_tenant_using_pagination(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_list)

        result = self.api.list(1, 10)
        self.assertIsInstance(result, PaginatedTenantDto)
        self.assertEqual(list(result.data), [self.expected_dto])  # type: ignore

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/tenants",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params={"page": 1, "limit": 10},
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_stream_tenant(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_list)

        result = self.api.stream()
        self.assertIsInstance(result, PaginationIterator)
        self.assertEqual(list(result), [self.expected_dto])  # type: ignore

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/tenants",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params={"page": 0, "limit": 10},
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_stream_with_multiple_pages_tenant(self, mock_request: mock.MagicMock) -> None:
        mock_request.side_effect = [
            MockResponse(
                200, {"page": 0, "hasMore": True, "pageSize": 10, "data": [self.tenant_json for _ in range(10)]}
            ),
            MockResponse(200, {"page": 1, "hasMore": False, "pageSize": 10, "data": [self.tenant_json]}),
        ]

        result = self.api.stream()
        self.assertIsInstance(result, PaginationIterator)
        self.assertEqual(list(result), [self.expected_dto for _ in range(11)])  # type: ignore

        mock_request.assert_any_call(
            method="GET",
            url="sample.novu.com/v1/tenants",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params={"page": 1, "limit": 10},
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_create_tenant(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(
            201, {"data": {"_id": "63e17e5b33a4f299199329b5", "identifier": "my-tenant", "name": "My Tenant"}}
        )

        res = self.api.create("my-tenant", "My Tenant")
        self.assertIsInstance(res, TenantDto)
        self.assertEqual(res._id, "63e17e5b33a4f299199329b5")
        self.assertEqual(res.identifier, "my-tenant")

        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/tenants",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json={"identifier": "my-tenant", "name": "My Tenant", "data": {}},
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_get_tenant(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_get)

        res = self.api.get("my-tenant")
        self.assertIsInstance(res, TenantDto)
        self.assertEqual(res._id, "63e17e5b33a4f299199329b5")
        self.assertEqual(res.identifier, "my-tenant")
        self.assertEqual(res.name, "My Tenant")

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/tenants/my-tenant",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_patch_tenant(self, mock_request: mock.MagicMock) -> None:
        res_patch = copy.deepcopy(self.response_get)
        res_patch["data"]["identifier"] = "new-tenant-ref"
        mock_request.return_value = MockResponse(200, res_patch)

        res = self.api.patch("my-tenant", identifier="new-tenant-ref")
        self.assertIsInstance(res, TenantDto)
        self.assertEqual(res._id, "63e17e5b33a4f299199329b5")
        self.assertEqual(res.identifier, "new-tenant-ref")
        self.assertEqual(res.name, "My Tenant")

        mock_request.assert_called_once_with(
            method="PATCH",
            url="sample.novu.com/v1/tenants/my-tenant",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json={"identifier": "new-tenant-ref"},
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_delete_tenant(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(204, raise_on_json_decode=True)

        self.assertIsNone(self.api.delete("my-tenant"))  # type: ignore

        mock_request.assert_called_once_with(
            method="DELETE",
            url="sample.novu.com/v1/tenants/my-tenant",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params=None,
            timeout=5,
        )
