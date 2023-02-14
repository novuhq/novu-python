import types
from unittest import TestCase, mock

from novu.api import ExecutionDetailApi
from novu.config import NovuConfig
from novu.dto import ExecutionDetailDto
from tests.factories import MockResponse


class ExecutionDetailApiTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        NovuConfig.configure("sample.novu.com", "api-key")
        cls.api = ExecutionDetailApi()

        cls.response_json = {
            "_id": "63eaba6ed1a5554c97dca0aa",
            "_jobId": "63eaba6ed1a5554c97dca0a3",
            "_environmentId": "63dafed97779f59258e38445",
            "_organizationId": "63dafed97779f59258e3843f",
            "_notificationId": "63eaba6ed1a5554c97dca098",
            "_notificationTemplateId": "63eab7dfd1a5554c97dc9088",
            "_subscriberId": "63dafedbc037e013fd82d37a",
            "providerId": "novu",
            "transactionId": "a8edd9ff-a18a-428a-be7c-57ef1aaf3d65",
            "channel": "in_app",
            "detail": "Step created",
            "source": "Internal",
            "status": "Pending",
            "isTest": False,
            "isRetry": False,
            "createdAt": "2023-02-13T22:32:14.733Z",
            "updatedAt": "2023-02-13T22:32:14.733Z",
            "__v": 0,
        }
        cls.expected_dto = ExecutionDetailDto(
            _id="63eaba6ed1a5554c97dca0aa",
            _job_id="63eaba6ed1a5554c97dca0a3",
            _environment_id="63dafed97779f59258e38445",
            _organization_id="63dafed97779f59258e3843f",
            _notification_id="63eaba6ed1a5554c97dca098",
            _notification_template_id="63eab7dfd1a5554c97dc9088",
            _subscriber_id="63dafedbc037e013fd82d37a",
            _message_id=None,
            provider_id="novu",
            transaction_id="a8edd9ff-a18a-428a-be7c-57ef1aaf3d65",
            channel="in_app",
            detail="Step created",
            source="Internal",
            status="Pending",
            is_test=False,
            is_retry=False,
            raw=None,
            created_at="2023-02-13T22:32:14.733Z",
            updated_at="2023-02-13T22:32:14.733Z",
        )

    @mock.patch("requests.request")
    def test_list_execution_details(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, {"data": [self.response_json]})

        res = self.api.list("63eaba6ed1a5554c97dca098", "63dafedbc037e013fd82d37a")
        self.assertIsInstance(res, types.GeneratorType)
        self.assertEqual(list(res), [self.expected_dto])

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/execution-details",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params={"notificationId": "63eaba6ed1a5554c97dca098", "subscriberId": "63dafedbc037e013fd82d37a"},
            timeout=5,
        )
