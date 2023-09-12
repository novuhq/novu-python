from unittest import TestCase, mock

from novu.api.notification import NotificationApi
from novu.config import NovuConfig
from novu.dto.notification import (
    ActivityNotificationDto,
    ActivityNotificationExecutionDetailResponseDto,
    ActivityNotificationJobResponseDto,
    ActivityNotificationStepResponseDto,
    ActivityNotificationSubscriberResponseDTO,
    ActivityNotificationTemplateResponseDto,
    ActivityNotificationTriggerResponseDto,
)
from tests.factories import MockResponse


class NotificationApiTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        NovuConfig.configure("sample.novu.com", "api-key")
        cls.api = NotificationApi()
        cls.notification_json = {
            "_id": "63dafed97779f59258e44954",
            "_environmentId": "63dafed97779f59258e38445",
            "_organizationId": "789er454569345",
            "transactionId": "fefrey56v",
            "createdAt": "2023-07-13",
            "channels": ["in_app"],
            "subscriber": {
                "firstName": "Max",
                "_id": "123",
                "lastName": "Moe",
                "email": "max.moe@example.com",
                "phone": "+441234567893",
            },
            "template": {
                "_id": "12crefr3",
                "name": "Template3",
                "triggers": [
                    {
                        "type": "type1",
                        "identifier": "identifier1",
                        "variables": [{"name": "variable4"}],
                        "subscriberVariables": [{"name": "subscribeVariable1"}],
                    }
                ],
            },
            "jobs": [
                {
                    "_id": "123vivie3",
                    "type": "Type1",
                    "digest": {},
                    "executionDetails": [
                        {
                            "_id": "123",
                            "_jobId": "456",
                            "status": "Success",
                            "detail": "Detail",
                            "isRetry": True,
                            "isTest": False,
                            "providerId": {},
                            "raw": "Raw",
                            "source": "Credentials",
                        }
                    ],
                    "step": {
                        "_id": "123",
                        "active": True,
                        "filters": {},
                        "template": {},
                    },
                    "payload": {},
                    "providerId": {},
                    "status": "completed",
                },
            ],
        }
        cls.response_notification = {"data": cls.notification_json}
        cls.expected_dto = ActivityNotificationDto(
            _id="63dafed97779f59258e44954",
            _environment_id="63dafed97779f59258e38445",
            _organization_id="789er454569345",
            transaction_id="fefrey56v",
            created_at="2023-07-13",
            channels=["in_app"],
            subscriber=ActivityNotificationSubscriberResponseDTO(
                first_name="Max",
                _id="123",
                last_name="Moe",
                email="max.moe@example.com",
                phone="+441234567893",
            ),
            template=ActivityNotificationTemplateResponseDto(
                _id="12crefr3",
                name="Template3",
                triggers=[
                    ActivityNotificationTriggerResponseDto(
                        type="type1",
                        identifier="identifier1",
                        variables=[{"name": "variable4"}],
                        subscriber_variables=[{"name": "subscriberVariable1"}],
                    ),
                ],
            ),
            jobs=[
                ActivityNotificationJobResponseDto(
                    _id="123vivie3",
                    type="Type1",
                    digest={},
                    execution_details=[
                        ActivityNotificationExecutionDetailResponseDto(
                            _id="123",
                            _job_id="456",
                            status="Success",
                            detail="Detail",
                            is_retry=True,
                            is_test=False,
                            provider_id={},
                            raw="Raw",
                            source="Credentials",
                        )
                    ],
                    step=[
                        ActivityNotificationStepResponseDto(
                            _id="123",
                            active=True,
                            filters={},
                            template={},
                        ),
                    ],
                    payload={},
                    provider_id={},
                    status="completed",
                )
            ],
        )

    @mock.patch("requests.request")
    def test_list(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_notification)

        channels = ["in_app"]
        templates = ["Template3"]
        emails = ["max.moe@example.com"]
        search = "example"
        notification_result = self.api.list(channels, templates, emails, search)

        self.assertIsInstance(notification_result, ActivityNotificationDto)
        self.assertEqual(notification_result._id, self.expected_dto._id)
        self.assertEqual(notification_result._environment_id, self.expected_dto._environment_id)
        self.assertEqual(notification_result._organization_id, self.expected_dto._organization_id)

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/notifications",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params={
                "channels": channels,
                "templates": templates,
                "emails": emails,
                "search": search,
                "page": 0,
                "transactionId": None,
            },
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_stats(self, mock_request: mock.MagicMock) -> None:
        response_stats = {"data": {"weeklySent": 100, "monthlySent": 500}}
        mock_request.return_value = MockResponse(200, response_stats)

        stats_result = self.api.stats(id="123", start_date="2023-07-01", end_date="2023-07-31")

        self.assertEqual(stats_result, response_stats)

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/notifications/stats",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params={"id": "123", "start_date": "2023-07-01", "end_date": "2023-07-31"},
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_graph_stats(self, mock_request: mock.MagicMock) -> None:
        response_graph_stats = {
            "data": [
                {
                    "_id": "123",
                    "count": 10,
                    "templates": ["Template1"],
                    "channels": ["in_app"],
                }
            ]
        }
        mock_request.return_value = MockResponse(200, response_graph_stats)

        graph_stats_result = self.api.graph_stats(id="123", start_date="2023-07-01", end_date="2023-07-31", days=7)

        self.assertEqual(graph_stats_result, response_graph_stats["data"])

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/notifications/graph/stats",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params={
                "id": "123",
                "start_date": "2023-07-01",
                "end_date": "2023-07-31",
                "days": 7,
            },
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_get(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_notification)
        notification_id = "63dafed97779f59258e44954"

        notification_result = self.api.get(notification_id)

        self.assertIsInstance(notification_result, ActivityNotificationDto)
        self.assertEqual(notification_result._id, self.expected_dto._id)
        self.assertEqual(notification_result._environment_id, self.expected_dto._environment_id)
        self.assertEqual(notification_result._organization_id, self.expected_dto._organization_id)

        mock_request.assert_called_once_with(
            method="GET",
            url=f"sample.novu.com/v1/notifications/{notification_id}",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params=None,
            timeout=5,
        )
