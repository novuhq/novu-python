from collections.abc import Generator
from unittest import TestCase, mock

from novu.api import NotificationGroupApi
from novu.config import NovuConfig
from novu.dto.notification_group import (
    NotificationGroupDto,
    PaginatedNotificationGroupDto,
)
from tests.factories import MockResponse


class NotificationGroupApiTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        NovuConfig.configure("sample.novu.com", "api-key")
        cls.api = NotificationGroupApi()
        cls.notification_group_json = {
            "_id": "63dafed97779f59258e38449",
            "name": "General",
            "_organizationId": "63dafed97779f59258e3843f",
            "_environmentId": "63dafed97779f59258e38445",
            "createdAt": "2023-02-02T00:07:53.951Z",
            "updatedAt": "2023-02-02T00:07:53.951Z",
            "__v": 0,
        }
        cls.response_list = {"page": 0, "totalCount": 1, "pageSize": 10, "data": [cls.notification_group_json]}
        cls.response_get = {"data": cls.notification_group_json}
        cls.expected_dto = NotificationGroupDto(
            name="General",
            _id="63dafed97779f59258e38449",
            _environment_id="63dafed97779f59258e38445",
            _organization_id="63dafed97779f59258e3843f",
            _parent_id=None,
            created_at="2023-02-02T00:07:53.951Z",
            updated_at="2023-02-02T00:07:53.951Z",
        )

    @mock.patch("requests.request")
    def test_list_notification_group(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_list)

        result = self.api.list()
        self.assertIsInstance(result, PaginatedNotificationGroupDto)
        self.assertEqual(list(result.data), [self.expected_dto])

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/notification-groups",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_create_notification_group(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(201, self.response_get)

        res = self.api.create("something")
        self.assertIsInstance(res, NotificationGroupDto)
        self.assertEqual(res, self.expected_dto)

        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/notification-groups",
            headers={"Authorization": "ApiKey api-key"},
            json={"name": "something"},
            params=None,
            timeout=5,
        )
