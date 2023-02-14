from unittest import TestCase, mock

from novu.api import MessageApi
from novu.config import NovuConfig
from novu.dto.message import MessageDto, PaginatedMessageDto
from novu.enums import Channel
from tests.factories import MockResponse


class MessageApiTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        NovuConfig.configure("sample.novu.com", "api-key")
        cls.api = MessageApi()

        cls.response_json = {
            "_id": "63daff4cc037e013fd82dadd",
            "_templateId": "63daff36c037e013fd82da05",
            "_environmentId": "63dafed97779f59258e38445",
            "_messageTemplateId": "63daff36c037e013fd82d9f4",
            "_notificationId": "63daff487779f59258e38b24",
            "_organizationId": "63dafed97779f59258e3843f",
            "_subscriberId": "63dafedbc037e013fd82d37a",
            "_jobId": "63daff4c7779f59258e38b3c",
            "templateIdentifier": "absences",
            "cta": {"action": {"buttons": []}},
            "_feedId": None,
            "channel": "in_app",
            "content": "test",
            "deviceTokens": [],
            "seen": True,
            "read": True,
            "status": "sent",
            "transactionId": "aa287682-cb30-4a5f-a03a-f28f59c9d46d",
            "deleted": False,
            "createdAt": "2023-02-02T00:09:48.673Z",
            "updatedAt": "2023-02-02T00:10:21.544Z",
            "__v": 0,
            "lastReadDate": "2023-02-02T00:10:21.544Z",
            "lastSeenDate": "2023-02-02T00:10:21.544Z",
        }
        cls.maxDiff = None
        cls.expected_dto = MessageDto(
            identifier=None,
            _id="63daff4cc037e013fd82dadd",
            _template_id="63daff36c037e013fd82da05",
            _environment_id="63dafed97779f59258e38445",
            _message_template_id="63daff36c037e013fd82d9f4",
            _organization_id="63dafed97779f59258e3843f",
            _subscriber_id="63dafedbc037e013fd82d37a",
            _job_id="63daff4c7779f59258e38b3c",
            template_identifier="absences",
            email=None,
            subject=None,
            cta={"action": {"buttons": []}},
            channel="in_app",
            content="test",
            provider_id=None,
            device_tokens=[],
            seen=True,
            read=True,
            status="sent",
            transaction_id="aa287682-cb30-4a5f-a03a-f28f59c9d46d",
            payload=None,
            created_at="2023-02-02T00:09:48.673Z",
            updated_at="2023-02-02T00:10:21.544Z",
            deleted=False,
            last_read_date="2023-02-02T00:10:21.544Z",
            last_seen_date="2023-02-02T00:10:21.544Z",
        )

    @mock.patch("requests.request")
    def test_list_messages(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, {"data": [self.response_json]})

        res = self.api.list()
        self.assertIsInstance(res, PaginatedMessageDto)
        self.assertEqual(list(res.data), [self.expected_dto])

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/messages",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params={"limit": 10, "page": 0},
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_list_messages_with_filters(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, {"data": [self.response_json]})

        res = self.api.list(10, 0, Channel.IN_APP.value, "63dafedbc037e013fd82d37a")
        self.assertIsInstance(res, PaginatedMessageDto)
        self.assertEqual(list(res.data), [self.expected_dto])

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/messages",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params={"limit": 10, "page": 0, "channel": "in_app", "subscriberId": "63dafedbc037e013fd82d37a"},
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_delete_message(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, {"data": {"acknowledged": True, "status": "deleted"}})

        res = self.api.delete("63e969fcb6729e21337e2360")
        self.assertIsInstance(res, bool)
        self.assertTrue(res)

        mock_request.assert_called_once_with(
            method="DELETE",
            url="sample.novu.com/v1/messages/63e969fcb6729e21337e2360",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params=None,
            timeout=5,
        )
