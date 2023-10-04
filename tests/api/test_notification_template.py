from unittest import TestCase, mock

from novu.api import NotificationTemplateApi
from novu.api.base import PaginationIterator
from novu.config import NovuConfig
from novu.dto import (
    NotificationGroupDto,
    NotificationStepDto,
    NotificationTemplateDto,
    NotificationTemplateFormDto,
    NotificationTriggerDto,
    NotificationTriggerVariableDto,
    PaginatedNotificationTemplateDto,
    StepFilterDto,
    SubscriberPreferenceChannelDto,
)
from tests.factories import MockResponse


class NotificationTemplateApiTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        NovuConfig.configure("sample.novu.com", "api-key")
        cls.api = NotificationTemplateApi()
        cls.notification_template_json = {
            "preferenceSettings": {"email": True, "sms": True, "in_app": True, "chat": True, "push": True},
            "_id": "63daff36c037e013fd82da05",
            "name": "Absences",
            "active": True,
            "draft": False,
            "critical": False,
            "isBlueprint": False,
            "_notificationGroupId": "63dafed97779f59258e38449",
            "tags": [],
            "triggers": [
                {
                    "type": "event",
                    "identifier": "absences",
                    "variables": [],
                    "subscriberVariables": [{"name": "email", "_id": "63daff36c037e013fd82da07"}],
                    "_id": "63daff36c037e013fd82da06",
                }
            ],
            "steps": [
                {
                    "active": True,
                    "shouldStopOnFail": False,
                    "filters": [{"children": [], "_id": "63daff36c037e013fd82da09"}],
                    "_templateId": "63daff36c037e013fd82d9f4",
                    "_parentId": None,
                    "_id": "63daff36c037e013fd82d9f4",
                    "id": "63daff36c037e013fd82d9f4",
                },
                {
                    "active": True,
                    "shouldStopOnFail": False,
                    "filters": [{"children": [], "_id": "63daff36c037e013fd82da0b"}],
                    "_templateId": "63daff36c037e013fd82d9fc",
                    "_parentId": "63daff36c037e013fd82d9f4",
                    "_id": "63daff36c037e013fd82d9fc",
                    "id": "63daff36c037e013fd82d9fc",
                },
            ],
            "_environmentId": "63dafed97779f59258e38445",
            "_organizationId": "63dafed97779f59258e3843f",
            "_creatorId": "63dafed4117f8c850991ec4a",
            "deleted": False,
            "createdAt": "2023-02-02T00:09:26.080Z",
            "updatedAt": "2023-02-02T00:09:26.080Z",
            "__v": 0,
            "notificationGroup": {
                "_id": "63dafed97779f59258e38449",
                "name": "General",
                "_organizationId": "63dafed97779f59258e3843f",
                "_environmentId": "63dafed97779f59258e38445",
                "createdAt": "2023-02-02T00:07:53.951Z",
                "updatedAt": "2023-02-02T00:07:53.951Z",
                "__v": 0,
                "id": "63dafed97779f59258e38449",
            },
            "id": "63daff36c037e013fd82da05",
        }
        cls.response_list = {"page": 0, "totalCount": 1, "pageSize": 10, "data": [cls.notification_template_json]}
        cls.response_get = {"data": cls.notification_template_json}
        cls.expected_dto = NotificationTemplateDto(
            name="Absences",
            description=None,
            tags=[],
            steps=[
                NotificationStepDto(
                    _id="63daff36c037e013fd82d9f4",
                    _template_id="63daff36c037e013fd82d9f4",
                    _parent_id=None,
                    active=True,
                    should_stop_on_fail=False,
                    template=None,
                    filters=[StepFilterDto(is_negated=None, type=None, value=None, children=[])],
                    metadata=None,
                    replay_callback=None,
                ),
                NotificationStepDto(
                    _id="63daff36c037e013fd82d9fc",
                    _template_id="63daff36c037e013fd82d9fc",
                    _parent_id="63daff36c037e013fd82d9f4",
                    active=True,
                    should_stop_on_fail=False,
                    template=None,
                    filters=[StepFilterDto(is_negated=None, type=None, value=None, children=[])],
                    metadata=None,
                    replay_callback=None,
                ),
            ],
            active=True,
            critical=False,
            draft=False,
            preference_settings=SubscriberPreferenceChannelDto(email=True, sms=True, in_app=True, chat=True, push=True),
            triggers=[
                NotificationTriggerDto(
                    type="event",
                    identifier="absences",
                    variables=[],
                    subscriber_variables=[NotificationTriggerVariableDto(name="email")],
                )
            ],
            _id="63daff36c037e013fd82da05",
            _environment_id="63dafed97779f59258e38445",
            _organization_id="63dafed97779f59258e3843f",
            _notification_group_id="63dafed97779f59258e38449",
            _parent_id=None,
            _creator_id="63dafed4117f8c850991ec4a",
            notification_group=NotificationGroupDto(
                name="General",
                _id="63dafed97779f59258e38449",
                _environment_id="63dafed97779f59258e38445",
                _organization_id="63dafed97779f59258e3843f",
                _parent_id=None,
                created_at="2023-02-02T00:07:53.951Z",
                updated_at="2023-02-02T00:07:53.951Z",
            ),
            created_at="2023-02-02T00:09:26.080Z",
            updated_at="2023-02-02T00:09:26.080Z",
            deleted_at=None,
            deleted=False,
        )

    @mock.patch("requests.request")
    def test_list_notification_template(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_list)

        result = self.api.list()
        self.assertIsInstance(result, PaginatedNotificationTemplateDto)
        self.assertEqual(list(result.data), [self.expected_dto])

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/notification-templates",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params={},
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_list_notification_template_with_pagination(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_list)

        result = self.api.list(1, 10)
        self.assertIsInstance(result, PaginatedNotificationTemplateDto)
        self.assertEqual(list(result.data), [self.expected_dto])

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/notification-templates",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params={"page": 1, "limit": 10},
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_stream_notification_template(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_list)

        result = self.api.stream()
        self.assertIsInstance(result, PaginationIterator)
        self.assertEqual(list(result), [self.expected_dto])

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/notification-templates",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params={"page": 0, "limit": 10},
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_create_notification_template(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(201, self.response_get)

        result = self.api.create(
            NotificationTemplateFormDto(
                name="Absences",
                description=None,
                tags=[],
                steps=[
                    NotificationStepDto(
                        _id="63daff36c037e013fd82d9f4",
                        _template_id="63daff36c037e013fd82d9f4",
                        _parent_id=None,
                        active=True,
                        should_stop_on_fail=False,
                        template=None,
                        filters=[StepFilterDto(is_negated=None, type=None, value=None, children=[])],
                        metadata=None,
                        replay_callback=None,
                    ),
                    NotificationStepDto(
                        _id="63daff36c037e013fd82d9fc",
                        _template_id="63daff36c037e013fd82d9fc",
                        _parent_id="63daff36c037e013fd82d9f4",
                        active=True,
                        should_stop_on_fail=False,
                        template=None,
                        filters=[StepFilterDto(is_negated=None, type=None, value=None, children=[])],
                        metadata=None,
                        replay_callback=None,
                    ),
                ],
                active=True,
                critical=False,
                draft=False,
                preference_settings=SubscriberPreferenceChannelDto(
                    email=True, sms=True, in_app=True, chat=True, push=True
                ),
                notification_group_id="63dafed97779f59258e38449",
            )
        )
        self.assertIsInstance(result, NotificationTemplateDto)
        self.assertEqual(result, self.expected_dto)

        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/notification-templates",
            headers={"Authorization": "ApiKey api-key"},
            json={
                "name": "Absences",
                "notificationGroupId": "63dafed97779f59258e38449",
                "description": None,
                "tags": [],
                "steps": [
                    {
                        "_id": "63daff36c037e013fd82d9f4",
                        "_template_id": "63daff36c037e013fd82d9f4",
                        "_parent_id": None,
                        "active": True,
                        "should_stop_on_fail": False,
                        "template": None,
                        "filters": [{"is_negated": None, "type": None, "value": None, "children": []}],
                        "metadata": None,
                        "replay_callback": None,
                    },
                    {
                        "_id": "63daff36c037e013fd82d9fc",
                        "_template_id": "63daff36c037e013fd82d9fc",
                        "_parent_id": "63daff36c037e013fd82d9f4",
                        "active": True,
                        "should_stop_on_fail": False,
                        "template": None,
                        "filters": [{"is_negated": None, "type": None, "value": None, "children": []}],
                        "metadata": None,
                        "replay_callback": None,
                    },
                ],
                "active": True,
                "critical": False,
                "draft": False,
                "preferenceSettings": {"email": True, "sms": True, "in_app": True, "chat": True, "push": True},
            },
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_get_notification_template(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_get)

        result = self.api.get("63daff36c037e013fd82d9fc")
        self.assertIsInstance(result, NotificationTemplateDto)
        self.assertEqual(result, self.expected_dto)

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/notification-templates/63daff36c037e013fd82d9fc",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_update_notification_template(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_get)

        result = self.api.update(
            "63daff36c037e013fd82d9fc",
            NotificationTemplateFormDto(
                name="Absences",
                description=None,
                tags=[],
                steps=[
                    NotificationStepDto(
                        _id="63daff36c037e013fd82d9f4",
                        _template_id="63daff36c037e013fd82d9f4",
                        _parent_id=None,
                        active=True,
                        should_stop_on_fail=False,
                        template=None,
                        filters=[StepFilterDto(is_negated=None, type=None, value=None, children=[])],
                        metadata=None,
                        replay_callback=None,
                    ),
                    NotificationStepDto(
                        _id="63daff36c037e013fd82d9fc",
                        _template_id="63daff36c037e013fd82d9fc",
                        _parent_id="63daff36c037e013fd82d9f4",
                        active=True,
                        should_stop_on_fail=False,
                        template=None,
                        filters=[StepFilterDto(is_negated=None, type=None, value=None, children=[])],
                        metadata=None,
                        replay_callback=None,
                    ),
                ],
                active=True,
                critical=False,
                draft=False,
                preference_settings=SubscriberPreferenceChannelDto(
                    email=True, sms=True, in_app=True, chat=True, push=True
                ),
                notification_group_id="63dafed97779f59258e38449",
            ),
        )
        self.assertIsInstance(result, NotificationTemplateDto)
        self.assertEqual(result, self.expected_dto)

        mock_request.assert_called_once_with(
            method="PUT",
            url="sample.novu.com/v1/notification-templates/63daff36c037e013fd82d9fc",
            headers={"Authorization": "ApiKey api-key"},
            json={
                "name": "Absences",
                "notificationGroupId": "63dafed97779f59258e38449",
                "description": None,
                "tags": [],
                "steps": [
                    {
                        "_id": "63daff36c037e013fd82d9f4",
                        "_template_id": "63daff36c037e013fd82d9f4",
                        "_parent_id": None,
                        "active": True,
                        "should_stop_on_fail": False,
                        "template": None,
                        "filters": [{"is_negated": None, "type": None, "value": None, "children": []}],
                        "metadata": None,
                        "replay_callback": None,
                    },
                    {
                        "_id": "63daff36c037e013fd82d9fc",
                        "_template_id": "63daff36c037e013fd82d9fc",
                        "_parent_id": "63daff36c037e013fd82d9f4",
                        "active": True,
                        "should_stop_on_fail": False,
                        "template": None,
                        "filters": [{"is_negated": None, "type": None, "value": None, "children": []}],
                        "metadata": None,
                        "replay_callback": None,
                    },
                ],
                "active": True,
                "critical": False,
                "draft": False,
                "preferenceSettings": {"email": True, "sms": True, "in_app": True, "chat": True, "push": True},
            },
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_delete_notification_template(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(204, raise_on_json_decode=True)

        result = self.api.delete("63daff36c037e013fd82d9fc")
        self.assertIsNone(result)

        mock_request.assert_called_once_with(
            method="DELETE",
            url="sample.novu.com/v1/notification-templates/63daff36c037e013fd82d9fc",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_update_status_notification_template(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_get)

        result = self.api.update_status("63daff36c037e013fd82d9fc", True)
        self.assertIsInstance(result, NotificationTemplateDto)
        self.assertEqual(result, self.expected_dto)

        mock_request.assert_called_once_with(
            method="PUT",
            url="sample.novu.com/v1/notification-templates/63daff36c037e013fd82d9fc/status",
            headers={"Authorization": "ApiKey api-key"},
            json={"active": True},
            params=None,
            timeout=5,
        )
