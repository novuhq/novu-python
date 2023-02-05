from unittest import TestCase, mock

from novu.api import EventApi
from novu.config import NovuConfig
from novu.dto.event import EventDto
from novu.dto.topic import TriggerTopicDto
from novu.enums import EventStatus
from tests.factories import MockResponse


class EventApiTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        NovuConfig.configure("sample.novu.com", "api-key")
        cls.api = EventApi()

    @mock.patch("requests.request")
    def test_trigger_with_single_recipient(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(
            201, {"data": {"acknowledged": True, "status": EventStatus.PROCESSED.value, "transactionId": "sample-test"}}
        )

        result = self.api.trigger("test-template", "sample-recipient", {})

        self.assertIsInstance(result, EventDto)
        self.assertTrue(result.acknowledged)
        self.assertEqual(result.status, EventStatus.PROCESSED.value)
        self.assertEqual(result.transaction_id, "sample-test")
        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/events/trigger",
            headers={"Authorization": "ApiKey api-key"},
            json={"name": "test-template", "to": "sample-recipient", "payload": {}},
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_trigger_with_multiple_recipients(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(
            201, {"data": {"acknowledged": True, "status": EventStatus.PROCESSED.value, "transactionId": "sample-test"}}
        )

        result = self.api.trigger("test-template", ["sample-recipient-1", "sample-recipient-2"], {})

        self.assertIsInstance(result, EventDto)
        self.assertTrue(result.acknowledged)
        self.assertEqual(result.status, EventStatus.PROCESSED.value)
        self.assertEqual(result.transaction_id, "sample-test")
        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/events/trigger",
            headers={"Authorization": "ApiKey api-key"},
            json={"name": "test-template", "to": ["sample-recipient-1", "sample-recipient-2"], "payload": {}},
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_trigger_with_overrides(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(
            201, {"data": {"acknowledged": True, "status": EventStatus.PROCESSED.value, "transactionId": "sample-test"}}
        )

        result = self.api.trigger("test-template", "sample-recipient", {}, {"an": "override"})

        self.assertIsInstance(result, EventDto)
        self.assertTrue(result.acknowledged)
        self.assertEqual(result.status, EventStatus.PROCESSED.value)
        self.assertEqual(result.transaction_id, "sample-test")
        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/events/trigger",
            headers={"Authorization": "ApiKey api-key"},
            json={"name": "test-template", "to": "sample-recipient", "payload": {}, "overrides": {"an": "override"}},
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_trigger_with_actor(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(
            201, {"data": {"acknowledged": True, "status": EventStatus.PROCESSED.value, "transactionId": "sample-test"}}
        )

        result = self.api.trigger("test-template", "sample-recipient", {}, actor="actor-id")

        self.assertIsInstance(result, EventDto)
        self.assertTrue(result.acknowledged)
        self.assertEqual(result.status, EventStatus.PROCESSED.value)
        self.assertEqual(result.transaction_id, "sample-test")
        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/events/trigger",
            headers={"Authorization": "ApiKey api-key"},
            json={"name": "test-template", "to": "sample-recipient", "payload": {}, "actor": "actor-id"},
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_trigger_with_transaction_id(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(
            201, {"data": {"acknowledged": True, "status": EventStatus.PROCESSED.value, "transactionId": "sample-test"}}
        )

        result = self.api.trigger("test-template", "sample-recipient", {}, transaction_id="sample-test")

        self.assertIsInstance(result, EventDto)
        self.assertTrue(result.acknowledged)
        self.assertEqual(result.status, EventStatus.PROCESSED.value)
        self.assertEqual(result.transaction_id, "sample-test")
        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/events/trigger",
            headers={"Authorization": "ApiKey api-key"},
            json={"name": "test-template", "to": "sample-recipient", "payload": {}, "transactionId": "sample-test"},
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_trigger_topic_with_single_topic(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(
            201, {"data": {"acknowledged": True, "status": EventStatus.PROCESSED.value, "transactionId": "sample-test"}}
        )

        topic = TriggerTopicDto("topic-key", "type")
        result = self.api.trigger_topic("test-template", topic, {})

        self.assertIsInstance(result, EventDto)
        self.assertTrue(result.acknowledged)
        self.assertEqual(result.status, EventStatus.PROCESSED.value)
        self.assertEqual(result.transaction_id, "sample-test")
        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/events/trigger",
            headers={"Authorization": "ApiKey api-key"},
            json={"name": "test-template", "to": [{"topicKey": "topic-key", "type": "type"}], "payload": {}},
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_trigger_topic_with_multiple_topics(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(
            201, {"data": {"acknowledged": True, "status": EventStatus.PROCESSED.value, "transactionId": "sample-test"}}
        )

        topic_1 = TriggerTopicDto("topic-key-1", "type")
        topic_2 = TriggerTopicDto("topic-key-2", "type")
        result = self.api.trigger_topic("test-template", [topic_1, topic_2], {})

        self.assertIsInstance(result, EventDto)
        self.assertTrue(result.acknowledged)
        self.assertEqual(result.status, EventStatus.PROCESSED.value)
        self.assertEqual(result.transaction_id, "sample-test")
        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/events/trigger",
            headers={"Authorization": "ApiKey api-key"},
            json={
                "name": "test-template",
                "to": [{"topicKey": "topic-key-1", "type": "type"}, {"topicKey": "topic-key-2", "type": "type"}],
                "payload": {},
            },
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_trigger_topic_with_overrides(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(
            201, {"data": {"acknowledged": True, "status": EventStatus.PROCESSED.value, "transactionId": "sample-test"}}
        )

        topic = TriggerTopicDto("topic-key", "type")
        result = self.api.trigger_topic("test-template", topic, {}, {"an": "override"})

        self.assertIsInstance(result, EventDto)
        self.assertTrue(result.acknowledged)
        self.assertEqual(result.status, EventStatus.PROCESSED.value)
        self.assertEqual(result.transaction_id, "sample-test")
        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/events/trigger",
            headers={"Authorization": "ApiKey api-key"},
            json={
                "name": "test-template",
                "to": [{"topicKey": "topic-key", "type": "type"}],
                "payload": {},
                "overrides": {"an": "override"},
            },
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_trigger_topic_with_actor(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(
            201, {"data": {"acknowledged": True, "status": EventStatus.PROCESSED.value, "transactionId": "sample-test"}}
        )

        topic = TriggerTopicDto("topic-key", "type")
        result = self.api.trigger_topic("test-template", topic, {}, actor="actor-id")

        self.assertIsInstance(result, EventDto)
        self.assertTrue(result.acknowledged)
        self.assertEqual(result.status, EventStatus.PROCESSED.value)
        self.assertEqual(result.transaction_id, "sample-test")
        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/events/trigger",
            headers={"Authorization": "ApiKey api-key"},
            json={
                "name": "test-template",
                "to": [{"topicKey": "topic-key", "type": "type"}],
                "payload": {},
                "actor": "actor-id",
            },
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_trigger_topic_with_transaction_id(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(
            201, {"data": {"acknowledged": True, "status": EventStatus.PROCESSED.value, "transactionId": "sample-test"}}
        )

        topic = TriggerTopicDto("topic-key", "type")
        result = self.api.trigger_topic("test-template", topic, {}, transaction_id="sample-test")

        self.assertIsInstance(result, EventDto)
        self.assertTrue(result.acknowledged)
        self.assertEqual(result.status, EventStatus.PROCESSED.value)
        self.assertEqual(result.transaction_id, "sample-test")
        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/events/trigger",
            headers={"Authorization": "ApiKey api-key"},
            json={
                "name": "test-template",
                "to": [{"topicKey": "topic-key", "type": "type"}],
                "payload": {},
                "transactionId": "sample-test",
            },
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_broadcast_with_overrides(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(
            201, {"data": {"acknowledged": True, "status": EventStatus.PROCESSED.value, "transactionId": "sample-test"}}
        )

        result = self.api.broadcast("test-template", {}, {"an": "override"})

        self.assertIsInstance(result, EventDto)
        self.assertTrue(result.acknowledged)
        self.assertEqual(result.status, EventStatus.PROCESSED.value)
        self.assertEqual(result.transaction_id, "sample-test")
        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/events/trigger/broadcast",
            headers={"Authorization": "ApiKey api-key"},
            json={
                "name": "test-template",
                "payload": {},
                "overrides": {"an": "override"},
            },
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_broadcast_with_actor(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(
            201, {"data": {"acknowledged": True, "status": EventStatus.PROCESSED.value, "transactionId": "sample-test"}}
        )

        result = self.api.broadcast("test-template", {}, actor="actor-id")

        self.assertIsInstance(result, EventDto)
        self.assertTrue(result.acknowledged)
        self.assertEqual(result.status, EventStatus.PROCESSED.value)
        self.assertEqual(result.transaction_id, "sample-test")
        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/events/trigger/broadcast",
            headers={"Authorization": "ApiKey api-key"},
            json={
                "name": "test-template",
                "payload": {},
                "actor": "actor-id",
            },
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_broadcast_with_transaction_id(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(
            201, {"data": {"acknowledged": True, "status": EventStatus.PROCESSED.value, "transactionId": "sample-test"}}
        )

        result = self.api.broadcast("test-template", {}, transaction_id="sample-test")

        self.assertIsInstance(result, EventDto)
        self.assertTrue(result.acknowledged)
        self.assertEqual(result.status, EventStatus.PROCESSED.value)
        self.assertEqual(result.transaction_id, "sample-test")
        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/events/trigger/broadcast",
            headers={"Authorization": "ApiKey api-key"},
            json={
                "name": "test-template",
                "payload": {},
                "transactionId": "sample-test",
            },
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_delete(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200)

        self.assertIsNone(self.api.delete("sample-test"))

        mock_request.assert_called_once_with(
            method="DELETE",
            url="sample.novu.com/v1/events/trigger/sample-test",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params=None,
            timeout=5,
        )
