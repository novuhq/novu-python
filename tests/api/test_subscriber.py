from collections.abc import Generator
from unittest import TestCase, mock

import pkg_resources

from novu.api import SubscriberApi
from novu.api.base import PaginationIterator
from novu.config import NovuConfig
from novu.dto.subscriber import (
    BulkResultSubscriberDto,
    PaginatedSubscriberDto,
    SubscriberChannelSettingsCredentialsDto,
    SubscriberChannelSettingsDto,
    SubscriberDto,
    SubscriberPreferenceChannelDto,
    SubscriberPreferenceDto,
    SubscriberPreferencePreferenceDto,
    SubscriberPreferenceTemplateDto,
)
from novu.enums import Channel, ChatProviderIdEnum
from tests.factories import MockResponse

__version__ = pkg_resources.get_distribution("novu").version


class SubscriberApiTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        NovuConfig.configure("sample.novu.com", "api-key")
        cls.api = SubscriberApi()
        cls.subscriber_json = {
            "_id": "63dafedbc037e013fd82d37a",
            "_organizationId": "63dafed97779f59258e3843f",
            "_environmentId": "63dafed97779f59258e38445",
            "subscriberId": "63dafed4117f8c850991ec4a",
            "channels": [],
            "deleted": False,
            "createdAt": "2023-02-02T00:07:55.459Z",
            "updatedAt": "2023-02-06T23:03:22.645Z",
            "__v": 0,
            "isOnline": False,
            "lastOnlineAt": "2023-02-06T23:03:22.645Z",
        }
        cls.response_list = {
            "page": 0,
            "totalCount": 1,
            "pageSize": 10,
            "data": [cls.subscriber_json],
        }
        cls.response_get = {"data": cls.subscriber_json}
        cls.expected_dto = SubscriberDto(
            subscriber_id="63dafed4117f8c850991ec4a",
            first_name=None,
            last_name=None,
            phone=None,
            avatar=None,
            locale=None,
            _id="63dafedbc037e013fd82d37a",
            _environment_id="63dafed97779f59258e38445",
            _organization_id="63dafed97779f59258e3843f",
            channels=[],
            deleted=False,
            created_at="2023-02-02T00:07:55.459Z",
            updated_at="2023-02-06T23:03:22.645Z",
            is_online=False,
            last_online_at="2023-02-06T23:03:22.645Z",
        )

    @mock.patch("requests.request")
    def test_list_subscriber(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_list)

        result = self.api.list()
        self.assertIsInstance(result, PaginatedSubscriberDto)
        self.assertEqual(list(result.data), [self.expected_dto])

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/subscribers",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params={},
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_list_subscriber_using_pagination(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_list)

        result = self.api.list(1)
        self.assertIsInstance(result, PaginatedSubscriberDto)
        self.assertEqual(list(result.data), [self.expected_dto])

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/subscribers",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params={"page": 1},
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_stream_subscriber(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_list)

        result = self.api.stream()
        self.assertIsInstance(result, PaginationIterator)
        self.assertEqual(list(result), [self.expected_dto])

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/subscribers",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params={"page": 0, "limit": 10},
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_create_subscriber(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(
            201,
            {
                "data": {
                    "_organizationId": "63dafed97779f59258e3843f",
                    "_environmentId": "63dafed97779f59258e38445",
                    "firstName": None,
                    "lastName": None,
                    "phone": None,
                    "subscriberId": "subscriber-id",
                    "email": "subscriber@sample.com",
                    "avatar": None,
                    "locale": None,
                    "channels": [],
                    "_id": "63e2cc7151af34c4b2f2b5d1",
                    "deleted": False,
                    "createdAt": "2023-02-07T22:10:57.433Z",
                    "updatedAt": "2023-02-07T22:10:57.433Z",
                    "__v": 0,
                    "id": "63e2cc7151af34c4b2f2b5d1",
                }
            },
        )

        res = self.api.create(SubscriberDto("subscriber-id", "subscriber@sample.com"))
        self.assertIsInstance(res, SubscriberDto)
        self.assertEqual(res.subscriber_id, "subscriber-id")
        self.assertEqual(res.email, "subscriber@sample.com")

        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/subscribers",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json={
                "subscriberId": "subscriber-id",
                "email": "subscriber@sample.com",
                "firstName": None,
                "lastName": None,
                "phone": None,
                "avatar": None,
                "locale": None,
                "channels": None,
            },
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_bulk_create_subscribers(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(
            201,
            {
                "data": {
                    "created": [
                        {
                            "_organizationId": None,
                            "_environmentId": None,
                            "firstName": None,
                            "lastName": None,
                            "phone": None,
                            "subscriberId": "subscriber-id",
                            "email": "subscriber@sample.com",
                            "avatar": None,
                            "locale": None,
                            "channels": [],
                            "_id": "63e2cc7151af34c4b2f2b5d1",
                            "deleted": None,
                            "__v": 0,
                            "id": "63e2cc7151af34c4b2f2b5d1",
                        },
                        {
                            "_organizationId": None,
                            "_environmentId": None,
                            "firstName": None,
                            "lastName": None,
                            "phone": None,
                            "subscriberId": "subscriber1-id",
                            "email": "subscriber1@sample.com",
                            "avatar": None,
                            "locale": None,
                            "channels": [],
                            "_id": "63e2cc7151af34c4b2f2b5d2",
                            "deleted": None,
                            "__v": 0,
                            "id": "63e2cc7151af34c4b2f2b5d2",
                        },
                    ],
                    "updated": [],
                    "failed": [],
                }
            },
        )

        subscribers = [
            SubscriberDto(subscriber_id="subscriber-id", email="subscriber@sample.com"),
            SubscriberDto(subscriber_id="subscriber1-id", email="subscriber1@sample.com"),
        ]

        res = self.api.bulk_create(subscribers)

        self.assertIsInstance(res, BulkResultSubscriberDto)
        self.assertEqual(
            res,
            BulkResultSubscriberDto(
                created=[
                    SubscriberDto(
                        subscriber_id="subscriber-id",
                        email="subscriber@sample.com",
                        _id="63e2cc7151af34c4b2f2b5d1",
                        channels=[],
                    ),
                    SubscriberDto(
                        subscriber_id="subscriber1-id",
                        email="subscriber1@sample.com",
                        _id="63e2cc7151af34c4b2f2b5d2",
                        channels=[],
                    ),
                ],
                updated=[],
                failed=[],
            ),
        )

        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/subscribers/bulk",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json={
                "subscribers": [
                    {
                        "subscriberId": "subscriber-id",
                        "email": "subscriber@sample.com",
                        "firstName": None,
                        "lastName": None,
                        "phone": None,
                        "avatar": None,
                        "locale": None,
                        "channels": None,
                    },
                    {
                        "subscriberId": "subscriber1-id",
                        "email": "subscriber1@sample.com",
                        "firstName": None,
                        "lastName": None,
                        "phone": None,
                        "avatar": None,
                        "locale": None,
                        "channels": None,
                    },
                ]
            },
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_get_subscriber(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_get)

        res = self.api.get("subscriber-id")
        self.assertIsInstance(res, SubscriberDto)
        self.assertEqual(res, self.expected_dto)

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/subscribers/subscriber-id",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_get_subscriber_with_credentials_info(self, mock_request: mock.MagicMock) -> None:
        all_three = {
            "response": {"webhook_url": "TEST", "channel": "slack", "device_tokens": ["TEST"]},
            "expected": SubscriberChannelSettingsCredentialsDto(
                webhook_url="TEST", channel="slack", device_tokens=["TEST"]
            ),
        }
        only_webhook = {
            "response": {"webhook_url": "TEST"},
            "expected": SubscriberChannelSettingsCredentialsDto(webhook_url="TEST", channel=None, device_tokens=None),
        }
        only_channel = {
            "response": {"channel": "slack"},
            "expected": SubscriberChannelSettingsCredentialsDto(webhook_url=None, channel="slack", device_tokens=None),
        }
        only_device_tokens = {
            "response": {"device_tokens": ["TEST"]},
            "expected": SubscriberChannelSettingsCredentialsDto(webhook_url=None, channel=None, device_tokens=["TEST"]),
        }

        for test in [all_three, only_webhook, only_channel, only_device_tokens]:
            mock_request.return_value = MockResponse(
                200,
                {
                    "data": {
                        "_id": "63dafedbc037e013fd82d37a",
                        "_organizationId": "63dafed97779f59258e3843f",
                        "_environmentId": "63dafed97779f59258e38445",
                        "subscriberId": "63dafed4117f8c850991ec4a",
                        "channels": [
                            {
                                "provider_id": "slack",
                                "_integration_id": "64f6d74be166fcd7f2751111",
                                "credentials": test["response"],
                                "integration_identifier": None,
                            }
                        ],
                        "deleted": False,
                        "createdAt": "2023-02-02T00:07:55.459Z",
                        "updatedAt": "2023-02-06T23:03:22.645Z",
                        "__v": 0,
                        "isOnline": False,
                        "email": "oscar.marie-taillefer@spikeelabs.fr",
                        "lastOnlineAt": "2023-02-06T23:03:22.645Z",
                    }
                },
            )

            res = self.api.get("subscriber-id")
            self.assertIsInstance(res, SubscriberDto)
            self.assertEqual(
                res,
                SubscriberDto(
                    subscriber_id="63dafed4117f8c850991ec4a",
                    email="oscar.marie-taillefer@spikeelabs.fr",
                    first_name=None,
                    last_name=None,
                    phone=None,
                    avatar=None,
                    locale=None,
                    _id="63dafedbc037e013fd82d37a",
                    _environment_id="63dafed97779f59258e38445",
                    _organization_id="63dafed97779f59258e3843f",
                    channels=[
                        SubscriberChannelSettingsDto(
                            provider_id=ChatProviderIdEnum.SLACK,
                            _integration_id="64f6d74be166fcd7f2751111",
                            credentials=test["expected"],
                            integration_identifier=None,
                        )
                    ],
                    deleted=False,
                    created_at="2023-02-02T00:07:55.459Z",
                    updated_at="2023-02-06T23:03:22.645Z",
                    is_online=False,
                    last_online_at="2023-02-06T23:03:22.645Z",
                ),
            )

            mock_request.assert_called_once_with(
                method="GET",
                url="sample.novu.com/v1/subscribers/subscriber-id",
                headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
                json=None,
                params=None,
                timeout=5,
            )
            mock_request.reset_mock()

    @mock.patch("requests.request")
    def test_update_subscriber(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_get)

        res = self.api.put(SubscriberDto("subscriber-id", "subscriber@sample.com", "John", "Doe", "+33612345678"))
        self.assertIsInstance(res, SubscriberDto)
        self.assertEqual(res, self.expected_dto)

        mock_request.assert_called_once_with(
            method="PUT",
            url="sample.novu.com/v1/subscribers/subscriber-id",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json={
                "subscriberId": "subscriber-id",
                "email": "subscriber@sample.com",
                "firstName": "John",
                "lastName": "Doe",
                "phone": "+33612345678",
                "avatar": None,
                "locale": None,
                "channels": None,
            },
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_delete(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, {"data": {"acknowledged": True, "status": "deleted"}})

        self.api.delete("subscriber-id")

        mock_request.assert_called_once_with(
            method="DELETE",
            url="sample.novu.com/v1/subscribers/subscriber-id",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_credentials_update_webhook_url(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_get)

        res = self.api.credentials("subscriber-id", "slack", webhook_url="TEST")
        self.assertIsInstance(res, SubscriberDto)
        self.assertEqual(res, self.expected_dto)

        mock_request.assert_called_once_with(
            method="PUT",
            url="sample.novu.com/v1/subscribers/subscriber-id/credentials",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json={"providerId": "slack", "credentials": {"webhookUrl": "TEST"}},
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_credentials_update_device_tokens(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_get)

        res = self.api.credentials("subscriber-id", "slack", device_tokens=["TEST"])
        self.assertIsInstance(res, SubscriberDto)
        self.assertEqual(res, self.expected_dto)

        mock_request.assert_called_once_with(
            method="PUT",
            url="sample.novu.com/v1/subscribers/subscriber-id/credentials",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json={"providerId": "slack", "credentials": {"deviceTokens": ["TEST"]}},
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_online_status(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_get)

        res = self.api.online_status("subscriber-id", True)
        self.assertIsInstance(res, SubscriberDto)
        self.assertEqual(res, self.expected_dto)

        mock_request.assert_called_once_with(
            method="PATCH",
            url="sample.novu.com/v1/subscribers/subscriber-id/online-status",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json={"isOnline": True},
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_preferences(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(
            200,
            {
                "data": [
                    {
                        "template": {
                            "_id": "63daff36c037e013fd82da05",
                            "name": "Absences",
                            "critical": False,
                        },
                        "preference": {
                            "enabled": True,
                            "channels": {"email": True, "in_app": True},
                        },
                    }
                ]
            },
        )

        res = self.api.preferences("subscriber-id")
        self.assertIsInstance(res, Generator)
        self.assertEqual(
            list(res),
            [
                SubscriberPreferenceDto(
                    preference=SubscriberPreferencePreferenceDto(
                        enabled=True,
                        channels=SubscriberPreferenceChannelDto(email=True, in_app=True),
                    ),
                    template=SubscriberPreferenceTemplateDto(
                        _id="63daff36c037e013fd82da05", name="Absences", critical=False
                    ),
                )
            ],
        )

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/subscribers/subscriber-id/preferences",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_change_channel_preference(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(
            200,
            {
                "data": {
                    "template": {
                        "_id": "63daff36c037e013fd82da05",
                        "name": "Absences",
                        "critical": False,
                    },
                    "preference": {
                        "enabled": True,
                        "channels": {"email": True, "in_app": True},
                    },
                }
            },
        )

        res = self.api.change_channel_preference("subscriber-id", "63daff36c037e013fd82da05", "in_app", True)
        self.assertEqual(
            res,
            SubscriberPreferenceDto(
                preference=SubscriberPreferencePreferenceDto(
                    enabled=True,
                    channels=SubscriberPreferenceChannelDto(email=True, in_app=True),
                ),
                template=SubscriberPreferenceTemplateDto(
                    _id="63daff36c037e013fd82da05", name="Absences", critical=False
                ),
            ),
        )

        mock_request.assert_called_once_with(
            method="PATCH",
            url="sample.novu.com/v1/subscribers/subscriber-id/preferences/63daff36c037e013fd82da05",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json={"channel": {"type": "in_app", "enabled": True}},
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_change_channel_preference_using_enum_in_params(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(
            200,
            {
                "data": {
                    "template": {
                        "_id": "63daff36c037e013fd82da05",
                        "name": "Absences",
                        "critical": False,
                    },
                    "preference": {
                        "enabled": True,
                        "channels": {"email": True, "in_app": True},
                    },
                }
            },
        )

        res = self.api.change_channel_preference("subscriber-id", "63daff36c037e013fd82da05", Channel.IN_APP, True)
        self.assertEqual(
            res,
            SubscriberPreferenceDto(
                preference=SubscriberPreferencePreferenceDto(
                    enabled=True,
                    channels=SubscriberPreferenceChannelDto(email=True, in_app=True),
                ),
                template=SubscriberPreferenceTemplateDto(
                    _id="63daff36c037e013fd82da05", name="Absences", critical=False
                ),
            ),
        )

        mock_request.assert_called_once_with(
            method="PATCH",
            url="sample.novu.com/v1/subscribers/subscriber-id/preferences/63daff36c037e013fd82da05",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json={"channel": {"type": "in_app", "enabled": True}},
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_change_preference_state(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(
            200,
            {
                "data": {
                    "template": {
                        "_id": "63daff36c037e013fd82da05",
                        "name": "Absences",
                        "critical": False,
                    },
                    "preference": {
                        "enabled": False,
                        "channels": {"email": True, "in_app": True},
                    },
                }
            },
        )

        res = self.api.change_preference_state("subscriber-id", "63daff36c037e013fd82da05", False)
        self.assertEqual(
            res,
            SubscriberPreferenceDto(
                preference=SubscriberPreferencePreferenceDto(
                    enabled=False,
                    channels=SubscriberPreferenceChannelDto(email=True, in_app=True),
                ),
                template=SubscriberPreferenceTemplateDto(
                    _id="63daff36c037e013fd82da05", name="Absences", critical=False
                ),
            ),
        )

        mock_request.assert_called_once_with(
            method="PATCH",
            url="sample.novu.com/v1/subscribers/subscriber-id/preferences/63daff36c037e013fd82da05",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json={"enabled": False},
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_unseen_notifications(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, {"data": {"count": 0}})

        res = self.api.unseen_notifications("subscriber-id")
        self.assertEqual(res, 0)

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/subscribers/subscriber-id/notifications/unseen",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_delete_credentials(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(204)

        self.api.delete_credentials("subscriber-id", ChatProviderIdEnum.SLACK)

        mock_request.assert_called_once_with(
            method="DELETE",
            url="sample.novu.com/v1/subscribers/subscriber-id/credentials/slack",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params=None,
            timeout=5,
        )
