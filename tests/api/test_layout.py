from unittest import TestCase, mock

import pkg_resources

from novu.api import LayoutApi
from novu.config import NovuConfig
from novu.dto import LayoutDto, LayoutVariableDto, PaginatedLayoutDto
from tests.factories import MockResponse

__version__ = pkg_resources.get_distribution("novu").version


class LayoutApiTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        NovuConfig.configure("sample.novu.com", "api-key")
        cls.api = LayoutApi()
        cls.layout_json = {
            "_id": "63dafeda7779f59258e38450",
            "_environmentId": "63dafed97779f59258e38445",
            "_organizationId": "63dafed97779f59258e3843f",
            "_creatorId": "63dafed4117f8c850991ec4a",
            "identifier": "novu-default-layout",
            "name": "Default Layout",
            "description": "The default layout created by Novu",
            "variables": [
                {
                    "name": "branding.logo",
                    "type": "String",
                    "required": False,
                    "defaultValue": "",
                    "_id": "63dafeda7779f59258e38451",
                },
                {
                    "name": "preheader",
                    "type": "Boolean",
                    "required": False,
                    "defaultValue": True,
                    "_id": "63dafeda7779f59258e38452",
                },
                {
                    "name": "preheader",
                    "type": "String",
                    "required": False,
                    "defaultValue": "",
                    "_id": "63dafeda7779f59258e38453",
                },
                {
                    "name": "branding.color",
                    "type": "Boolean",
                    "required": False,
                    "defaultValue": True,
                    "_id": "63dafeda7779f59258e38454",
                },
                {
                    "name": "branding.color",
                    "type": "String",
                    "required": False,
                    "defaultValue": "",
                    "_id": "63dafeda7779f59258e38455",
                },
            ],
            "content": "",
            "contentType": "customHtml",
            "isDefault": True,
            "channel": "email",
            "deleted": False,
            "createdAt": "2023-02-02T00:07:54.022Z",
            "updatedAt": "2023-02-02T00:07:54.022Z",
            "__v": 0,
            "isDeleted": False,
        }
        cls.response_list = {"page": 0, "totalCount": 1, "pageSize": 10, "data": [cls.layout_json]}
        cls.response_get = {"data": cls.layout_json}
        cls.expected_dto = LayoutDto(
            name="Default Layout",
            identifier="novu-default-layout",
            description="The default layout created by Novu",
            content="",
            is_default=True,
            variables=[
                LayoutVariableDto(
                    name="branding.logo",
                    type="String",
                    _id="63dafeda7779f59258e38451",
                    required=False,
                    default_value="",
                ),
                LayoutVariableDto(
                    name="preheader", type="Boolean", _id="63dafeda7779f59258e38452", required=False, default_value=True
                ),
                LayoutVariableDto(
                    name="preheader", type="String", _id="63dafeda7779f59258e38453", required=False, default_value=""
                ),
                LayoutVariableDto(
                    name="branding.color",
                    type="Boolean",
                    _id="63dafeda7779f59258e38454",
                    required=False,
                    default_value=True,
                ),
                LayoutVariableDto(
                    name="branding.color",
                    type="String",
                    _id="63dafeda7779f59258e38455",
                    required=False,
                    default_value="",
                ),
            ],
            _id="63dafeda7779f59258e38450",
            _environment_id="63dafed97779f59258e38445",
            _organization_id="63dafed97779f59258e3843f",
            _creator_id="63dafed4117f8c850991ec4a",
            content_type="customHtml",
            channel="email",
            created_at="2023-02-02T00:07:54.022Z",
            updated_at="2023-02-02T00:07:54.022Z",
            is_deleted=False,
        )

    @mock.patch("requests.request")
    def test_list_layout(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_list)

        result = self.api.list()
        self.assertIsInstance(result, PaginatedLayoutDto)
        self.assertEqual(list(result.data), [self.expected_dto])

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/layouts",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params={"page": 0, "pageSize": 100},
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_list_layout_with_filters(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_list)

        result = self.api.list(page=1, limit=20)
        self.assertIsInstance(result, PaginatedLayoutDto)
        self.assertEqual(list(result.data), [self.expected_dto])

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/layouts",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params={"page": 1, "pageSize": 20},
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_create_layout(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_get)

        res = self.api.create(self.expected_dto)
        self.assertIsInstance(res, LayoutDto)
        self.assertEqual(res, self.expected_dto)

        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/layouts",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json={
                "name": "Default Layout",
                "identifier": "novu-default-layout",
                "description": "The default layout created by Novu",
                "content": "",
                "isDefault": True,
                "variables": [
                    {
                        "name": "branding.logo",
                        "type": "String",
                        "_id": "63dafeda7779f59258e38451",
                        "required": False,
                        "default_value": "",
                    },
                    {
                        "name": "preheader",
                        "type": "Boolean",
                        "_id": "63dafeda7779f59258e38452",
                        "required": False,
                        "default_value": True,
                    },
                    {
                        "name": "preheader",
                        "type": "String",
                        "_id": "63dafeda7779f59258e38453",
                        "required": False,
                        "default_value": "",
                    },
                    {
                        "name": "branding.color",
                        "type": "Boolean",
                        "_id": "63dafeda7779f59258e38454",
                        "required": False,
                        "default_value": True,
                    },
                    {
                        "name": "branding.color",
                        "type": "String",
                        "_id": "63dafeda7779f59258e38455",
                        "required": False,
                        "default_value": "",
                    },
                ],
            },
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_get_layout(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_get)

        res = self.api.get("63dafeda7779f59258e38450")
        self.assertIsInstance(res, LayoutDto)
        self.assertEqual(res, self.expected_dto)

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/layouts/63dafeda7779f59258e38450",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_patch_layout(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_get)

        res = self.api.patch(self.expected_dto)
        self.assertIsInstance(res, LayoutDto)
        self.assertEqual(res, self.expected_dto)

        mock_request.assert_called_once_with(
            method="PATCH",
            url="sample.novu.com/v1/layouts/63dafeda7779f59258e38450",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json={
                "name": "Default Layout",
                "identifier": "novu-default-layout",
                "description": "The default layout created by Novu",
                "content": "",
                "isDefault": True,
                "variables": [
                    {
                        "name": "branding.logo",
                        "type": "String",
                        "_id": "63dafeda7779f59258e38451",
                        "required": False,
                        "default_value": "",
                    },
                    {
                        "name": "preheader",
                        "type": "Boolean",
                        "_id": "63dafeda7779f59258e38452",
                        "required": False,
                        "default_value": True,
                    },
                    {
                        "name": "preheader",
                        "type": "String",
                        "_id": "63dafeda7779f59258e38453",
                        "required": False,
                        "default_value": "",
                    },
                    {
                        "name": "branding.color",
                        "type": "Boolean",
                        "_id": "63dafeda7779f59258e38454",
                        "required": False,
                        "default_value": True,
                    },
                    {
                        "name": "branding.color",
                        "type": "String",
                        "_id": "63dafeda7779f59258e38455",
                        "required": False,
                        "default_value": "",
                    },
                ],
            },
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_delete_layout(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(204, raise_on_json_decode=True)

        res = self.api.delete("63dafeda7779f59258e38450")
        self.assertIsNone(res)

        mock_request.assert_called_once_with(
            method="DELETE",
            url="sample.novu.com/v1/layouts/63dafeda7779f59258e38450",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_set_default_layout(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200)

        res = self.api.set_default("63dafeda7779f59258e38450")
        self.assertIsNone(res)

        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/layouts/63dafeda7779f59258e38450/default",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params=None,
            timeout=5,
        )
