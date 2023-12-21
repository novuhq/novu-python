from unittest import TestCase, mock

import pkg_resources

from novu.api import TopicApi
from novu.config import NovuConfig
from novu.dto.topic import PaginatedTopicDto, TopicDto
from tests.factories import MockResponse

__version__ = pkg_resources.get_distribution("novu").version


class TopicApiTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        NovuConfig.configure("sample.novu.com", "api-key")
        cls.api = TopicApi()
        cls.topic_json = {
            "_id": "63e17e5b33a4f299199329b5",
            "_environmentId": "63dafed97779f59258e38445",
            "_organizationId": "63dafed97779f59258e3843f",
            "key": "my-topic",
            "name": "My Topic",
            "subscribers": [],
        }
        cls.response_list = {"page": 0, "totalCount": 1, "pageSize": 10, "data": [cls.topic_json]}
        cls.response_get = {"data": cls.topic_json}
        cls.expected_dto = TopicDto(
            _id="63e17e5b33a4f299199329b5",
            _environment_id="63dafed97779f59258e38445",
            _organization_id="63dafed97779f59258e3843f",
            key="my-topic",
            name="My Topic",
            subscribers=[],
        )

    @mock.patch("requests.request")
    def test_list_topic(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_list)

        result = self.api.list()
        self.assertIsInstance(result, PaginatedTopicDto)
        self.assertEqual(list(result.data), [self.expected_dto])

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/topics",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params={},
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_list_topic_using_pagination(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_list)

        result = self.api.list(1, 10, "my-topic")
        self.assertIsInstance(result, PaginatedTopicDto)
        self.assertEqual(list(result.data), [self.expected_dto])

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/topics",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params={"page": 1, "limit": 10, "key": "my-topic"},
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_create_topic(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(201, {"data": {"_id": "63e17e5b33a4f299199329b5", "key": "my-topic"}})

        res = self.api.create("my-topic", "My Topic")
        self.assertIsInstance(res, TopicDto)
        self.assertEqual(res._id, "63e17e5b33a4f299199329b5")
        self.assertEqual(res.key, "my-topic")
        self.assertIsNone(res.name)

        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/topics",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json={"key": "my-topic", "name": "My Topic"},
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_get_topic(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_get)

        res = self.api.get("my-topic")
        self.assertIsInstance(res, TopicDto)
        self.assertEqual(res._id, "63e17e5b33a4f299199329b5")
        self.assertEqual(res.key, "my-topic")
        self.assertEqual(res.name, "My Topic")

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/topics/my-topic",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_subscribe_ok(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, {"data": {"succeeded": ["63dafed4117f8c850991ec4a"]}})

        succeed, failed = self.api.subscribe("my-topic", "63dafed4117f8c850991ec4a")
        self.assertEqual(succeed, ["63dafed4117f8c850991ec4a"])
        self.assertEqual(failed, {})

        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/topics/my-topic/subscribers",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json={"subscribers": ["63dafed4117f8c850991ec4a"]},
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_subscribe_with_ok_and_failed(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(
            200, {"data": {"succeeded": ["63dafed4117f8c850991ec4a"], "failed": {"notFound": ["not-defined"]}}}
        )

        succeed, failed = self.api.subscribe("my-topic", ["63dafed4117f8c850991ec4a", "not-defined"])
        self.assertEqual(succeed, ["63dafed4117f8c850991ec4a"])
        self.assertEqual(failed, {"notFound": ["not-defined"]})

        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/topics/my-topic/subscribers",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json={"subscribers": ["63dafed4117f8c850991ec4a", "not-defined"]},
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_unsubscribe_single_subscriber(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(204)

        self.api.unsubscribe("my-topic", "not-defined")

        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/topics/my-topic/subscribers/removal",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json={"subscribers": ["not-defined"]},
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_unsubscribe_multiple_subscribers(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(204)

        self.api.unsubscribe("my-topic", ["63dafed4117f8c850991ec4a", "not-defined"])

        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/topics/my-topic/subscribers/removal",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json={"subscribers": ["63dafed4117f8c850991ec4a", "not-defined"]},
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_rename_200(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_get)

        topic = self.api.rename("my-topic", "My Topic")
        self.assertIsInstance(topic, TopicDto)
        self.assertEqual(topic._id, "63e17e5b33a4f299199329b5")
        self.assertEqual(topic.name, "My Topic")

        mock_request.assert_called_once_with(
            method="PATCH",
            url="sample.novu.com/v1/topics/my-topic",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json={"name": "My Topic"},
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_delete(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(204)

        self.api.delete("my-topic")

        mock_request.assert_called_once_with(
            method="DELETE",
            url="sample.novu.com/v1/topics/my-topic",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params=None,
            timeout=5,
        )
