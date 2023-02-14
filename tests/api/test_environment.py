import types
from unittest import TestCase, mock

from novu.api import EnvironmentApi
from novu.config import NovuConfig
from novu.dto import EnvironmentApiKeyDto, EnvironmentDto, EnvironmentWidgetDto
from tests.factories import MockResponse


class EnvironmentApiTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        NovuConfig.configure("sample.novu.com", "api-key")
        cls.api = EnvironmentApi()

        cls.response_json_env = {
            "widget": {"notificationCenterEncryption": False},
            "_id": "63dafed97779f59258e38445",
            "name": "Development",
            "identifier": "IpfnHDLmHfKu",
            "_organizationId": "63dafed97779f59258e3843f",
            "createdAt": "2023-02-02T00:07:53.947Z",
            "updatedAt": "2023-02-04T15:36:57.631Z",
            "__v": 0,
            "id": "63dafed97779f59258e38445",
        }
        cls.response_json_api_key = {
            "key": "3rdxM3UdBDosZmEeLsDf9BErQYkXGB9m",
            "_userId": "63dafed4117f8c850991ec4a",
            "_id": "63de7b9933a4f299191f772b",
        }
        cls.expected_dto_env = EnvironmentDto(
            id="63dafed97779f59258e38445",
            _id="63dafed97779f59258e38445",
            name="Development",
            identifier="IpfnHDLmHfKu",
            _organization_id="63dafed97779f59258e3843f",
            widget=EnvironmentWidgetDto(notification_center_encryption=False),
            api_keys=None,
            created_at="2023-02-02T00:07:53.947Z",
            updated_at="2023-02-04T15:36:57.631Z",
        )
        cls.expected_dto_api_key = EnvironmentApiKeyDto(
            key="3rdxM3UdBDosZmEeLsDf9BErQYkXGB9m", _user_id="63dafed4117f8c850991ec4a", _id="63de7b9933a4f299191f772b"
        )
        cls.maxDiff = None

    @mock.patch("requests.request")
    def test_list_environments(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, {"data": [self.response_json_env]})

        res = self.api.list()
        self.assertIsInstance(res, types.GeneratorType)
        self.assertEqual(list(res), [self.expected_dto_env])

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/environments",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_create_environment(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(201, {"data": self.response_json_env})

        res = self.api.create("test")
        self.assertIsInstance(res, EnvironmentDto)
        self.assertEqual(res, self.expected_dto_env)

        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/environments",
            headers={"Authorization": "ApiKey api-key"},
            json={"name": "test"},
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_create_environment_with_parent_id(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(201, {"data": self.response_json_env})

        res = self.api.create("test", "parent_id")
        self.assertIsInstance(res, EnvironmentDto)
        self.assertEqual(res, self.expected_dto_env)

        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/environments",
            headers={"Authorization": "ApiKey api-key"},
            json={"name": "test", "parentId": "parent_id"},
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_get_current_environment(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(201, {"data": self.response_json_env})

        res = self.api.current()
        self.assertIsInstance(res, EnvironmentDto)
        self.assertEqual(res, self.expected_dto_env)

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/environments/me",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_list_environment_api_keys(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, {"data": [self.response_json_api_key]})

        res = self.api.api_keys()
        self.assertIsInstance(res, types.GeneratorType)
        self.assertEqual(list(res), [self.expected_dto_api_key])

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/environments/api-keys",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params=None,
            timeout=5,
        )
