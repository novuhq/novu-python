from unittest import TestCase, mock

from novu.api import BlueprintApi
from novu.config import NovuConfig
from novu.dto import BlueprintDto, GroupedBlueprintDto
from tests.factories import MockResponse


class BlueprintApiTests(TestCase):
    api: BlueprintApi
    blueprint_json = {
        "name": "Sample Blueprint",
        "description": "Sample Blueprint Description",
        "_id": "63dafeda7779f59258e38450",
        "_environmentId": "63dafed97779f59258e38445",
        "_organizationId": "63dafed97779f59258e3843f",
        "_notificationGroupId": "63dafed97779f59258e3844b",
        "_creatorId": "63dafed4117f8c850991ec4a",
        "blueprintId": "63dafeda7779f59258e38450",
        "createdAt": "2023-06-23T12:00:00.000Z",
        "updatedAt": "2023-06-23T12:00:00.000Z",
        "deleted": False,
        "deletedAt": None,
        "deletedBy": None,
    }

    grouped_blueprint_json = {
        "category": "example_category",
        "general": [blueprint_json],
        "popular": [blueprint_json],
    }

    response_get = {"data": blueprint_json}
    response_grouped = {"data": grouped_blueprint_json}
    expected_blueprint_dto = BlueprintDto(
        name="Sample Blueprint",
        description="Sample Blueprint Description",
        _id="63dafeda7779f59258e38450",
        _environment_id="63dafed97779f59258e38445",
        _organization_id="63dafed97779f59258e3843f",
        _notification_group_id="63dafed97779f59258e3844b",
        _creator_id="63dafed4117f8c850991ec4a",
        blueprint_id="63dafeda7779f59258e38450",
        created_at="2023-06-23T12:00:00.000Z",
        updated_at="2023-06-23T12:00:00.000Z",
        deleted=False,
        deleted_at=None,
        deleted_by=None,
    )
    expected_grouped_blueprint_dto = GroupedBlueprintDto(
        category="example_category",
        general=[expected_blueprint_dto],
        popular=[expected_blueprint_dto],
    )

    @classmethod
    def setUpClass(cls) -> None:
        NovuConfig.configure("sample.novu.com", "api-key")
        cls.api = BlueprintApi()

    @mock.patch("requests.request")
    def test_get_blueprint_by_id(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_get)

        result = self.api.get_by_id("63dafeda7779f59258e38450")
        self.assertIsInstance(result, BlueprintDto)
        self.assertEqual(result, self.expected_blueprint_dto)

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/blueprints/63dafeda7779f59258e38450",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_get_grouped_blueprints(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_grouped)

        result = self.api.get_grouped_by_category()
        self.assertIsInstance(result, GroupedBlueprintDto)
        self.assertEqual(result, self.expected_grouped_blueprint_dto)

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/blueprints/group-by-category",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params=None,
            timeout=5,
        )
