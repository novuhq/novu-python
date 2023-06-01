import types
from unittest import TestCase, mock

from novu.api import IntegrationApi
from novu.config import NovuConfig
from novu.dto.integration import IntegrationChannelUsageDto, IntegrationDto
from novu.enums import Channel, ChatProviderIdEnum, EmailProviderIdEnum
from tests.factories import MockResponse


class IntegrationApiTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        NovuConfig.configure("sample.novu.com", "api-key")
        cls.api = IntegrationApi()
        cls.integration_json = {
            "_id": "63dfe50ecac5cff328ca5d24",
            "_environmentId": "63dafed97779f59258e38445",
            "_organizationId": "63dafed97779f59258e3843f",
            "providerId": EmailProviderIdEnum.CUSTOM_SMTP,
            "channel": Channel.EMAIL,
            "credentials": {
                "user": "test",
                "password": "test",
                "host": "test.com",
                "port": "587",
                "from": "from@sample.com",
                "senderName": "sample",
            },
            "active": False,
            "deleted": False,
            "createdAt": "2023-02-05T17:19:10.826Z",
            "updatedAt": "2023-02-05T17:19:10.826Z",
            "__v": 0,
        }
        cls.response_list = {"data": [cls.integration_json]}
        cls.response_get = {"data": cls.integration_json}
        cls.expected_dto = IntegrationDto(
            provider_id=EmailProviderIdEnum.CUSTOM_SMTP,
            channel=Channel.EMAIL,
            credentials={
                "user": "test",
                "password": "test",
                "host": "test.com",
                "port": "587",
                "from": "from@sample.com",
                "senderName": "sample",
            },
            active=False,
            _id="63dfe50ecac5cff328ca5d24",
            _environment_id="63dafed97779f59258e38445",
            _organization_id="63dafed97779f59258e3843f",
            created_at="2023-02-05T17:19:10.826Z",
            updated_at="2023-02-05T17:19:10.826Z",
            deleted_at=None,
            deleted_by=None,
            deleted=False,
        )

    @mock.patch("requests.request")
    def test_list_no_result(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, {"data": []})

        result = self.api.list()
        self.assertIsInstance(result, types.GeneratorType)
        self.assertEqual(list(result), [])

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/integrations",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_list_with_results(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_list)

        result = self.api.list()
        self.assertIsInstance(result, types.GeneratorType)
        self.assertEqual(list(result), [self.expected_dto])

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/integrations",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_list_only_active_no_result(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, {"data": []})

        result = self.api.list(only_active=True)
        self.assertIsInstance(result, types.GeneratorType)
        self.assertEqual(list(result), [])

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/integrations/active",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_list_with_results(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_list)

        result = self.api.list(only_active=True)
        self.assertIsInstance(result, types.GeneratorType)
        self.assertEqual(list(result), [self.expected_dto])

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/integrations/active",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_create_with_check_by_default(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_get)

        result = self.api.create(
            IntegrationDto(
                provider_id=EmailProviderIdEnum.CUSTOM_SMTP,
                channel=Channel.EMAIL,
                credentials={
                    "user": "test",
                    "password": "test",
                    "host": "test.com",
                    "port": "587",
                    "from": "from@sample.com",
                    "senderName": "sample",
                },
                active=False,
            )
        )
        self.assertEqual(result, self.expected_dto)

        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/integrations",
            headers={"Authorization": "ApiKey api-key"},
            json={
                "providerId": EmailProviderIdEnum.CUSTOM_SMTP,
                "channel": Channel.EMAIL,
                "credentials": {
                    "user": "test",
                    "password": "test",
                    "host": "test.com",
                    "port": "587",
                    "from": "from@sample.com",
                    "senderName": "sample",
                },
                "active": False,
                "check": True,
            },
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_create_without_check(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_get)

        result = self.api.create(
            IntegrationDto(
                provider_id=EmailProviderIdEnum.CUSTOM_SMTP,
                channel=Channel.EMAIL,
                credentials={
                    "user": "test",
                    "password": "test",
                    "host": "test.com",
                    "port": "587",
                    "from": "from@sample.com",
                    "senderName": "sample",
                },
                active=False,
            ),
            check=False,
        )
        self.assertEqual(result, self.expected_dto)

        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/integrations",
            headers={"Authorization": "ApiKey api-key"},
            json={
                "providerId": EmailProviderIdEnum.CUSTOM_SMTP,
                "channel": Channel.EMAIL,
                "credentials": {
                    "user": "test",
                    "password": "test",
                    "host": "test.com",
                    "port": "587",
                    "from": "from@sample.com",
                    "senderName": "sample",
                },
                "active": False,
                "check": False,
            },
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_create_channel_without_credentials(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(
            200,
            {
                "data": {
                    "_id": "63dfe50ecac5cff328ca5d24",
                    "_environmentId": "63dafed97779f59258e38445",
                    "_organizationId": "63dafed97779f59258e3843f",
                    "providerId": ChatProviderIdEnum.MS_TEAMS,
                    "channel": Channel.CHAT,
                    "active": True,
                    "deleted": False,
                    "createdAt": "2023-02-05T17:19:10.826Z",
                    "updatedAt": "2023-02-05T17:19:10.826Z",
                    "__v": 0,
                }
            },
        )

        result = self.api.create(
            IntegrationDto(
                channel=Channel.CHAT,
                provider_id=ChatProviderIdEnum.MS_TEAMS,
                credentials={},
                active=True,
            ),
            check=False,
        )
        self.assertEqual(
            result,
            IntegrationDto(
                provider_id=ChatProviderIdEnum.MS_TEAMS,
                channel=Channel.CHAT,
                credentials=None,
                active=True,
                _id="63dfe50ecac5cff328ca5d24",
                _environment_id="63dafed97779f59258e38445",
                _organization_id="63dafed97779f59258e3843f",
                created_at="2023-02-05T17:19:10.826Z",
                updated_at="2023-02-05T17:19:10.826Z",
                deleted_at=None,
                deleted_by=None,
                deleted=False,
            ),
        )

        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/integrations",
            headers={"Authorization": "ApiKey api-key"},
            json={
                "providerId": ChatProviderIdEnum.MS_TEAMS,
                "channel": Channel.CHAT,
                "credentials": {},
                "active": True,
                "check": False,
            },
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_get_provider_status(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, {"data": True})

        result = self.api.status("something")
        self.assertEqual(result, True)

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/integrations/webhooks/provider/something/status",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_update_with_check_by_default(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_get)

        result = self.api.update(
            IntegrationDto(
                provider_id=EmailProviderIdEnum.CUSTOM_SMTP,
                channel=Channel.EMAIL,
                credentials={
                    "user": "test",
                    "password": "test",
                    "host": "test.com",
                    "port": "587",
                    "from": "from@sample.com",
                    "senderName": "sample",
                },
                active=False,
                _id="identifier",
            )
        )
        self.assertEqual(result, self.expected_dto)

        mock_request.assert_called_once_with(
            method="PUT",
            url="sample.novu.com/v1/integrations/identifier",
            headers={"Authorization": "ApiKey api-key"},
            json={
                "providerId": EmailProviderIdEnum.CUSTOM_SMTP,
                "channel": Channel.EMAIL,
                "credentials": {
                    "user": "test",
                    "password": "test",
                    "host": "test.com",
                    "port": "587",
                    "from": "from@sample.com",
                    "senderName": "sample",
                },
                "active": False,
                "check": True,
            },
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_update_without_check(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, self.response_get)

        result = self.api.update(
            IntegrationDto(
                provider_id=EmailProviderIdEnum.CUSTOM_SMTP,
                channel=Channel.EMAIL,
                credentials={
                    "user": "test",
                    "password": "test",
                    "host": "test.com",
                    "port": "587",
                    "from": "from@sample.com",
                    "senderName": "sample",
                },
                active=False,
                _id="identifier",
            ),
            check=False,
        )
        self.assertEqual(result, self.expected_dto)

        mock_request.assert_called_once_with(
            method="PUT",
            url="sample.novu.com/v1/integrations/identifier",
            headers={"Authorization": "ApiKey api-key"},
            json={
                "providerId": EmailProviderIdEnum.CUSTOM_SMTP,
                "channel": Channel.EMAIL,
                "credentials": {
                    "user": "test",
                    "password": "test",
                    "host": "test.com",
                    "port": "587",
                    "from": "from@sample.com",
                    "senderName": "sample",
                },
                "active": False,
                "check": False,
            },
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_delete(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200)

        result = self.api.delete("identifier")
        self.assertIsNone(result)

        mock_request.assert_called_once_with(
            method="DELETE",
            url="sample.novu.com/v1/integrations/identifier",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_limit(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, {"data": {"limit": 300, "count": 3}})

        result = self.api.limit(Channel.EMAIL)
        self.assertIsInstance(result, IntegrationChannelUsageDto)
        self.assertEqual(result.limit, 300)
        self.assertEqual(result.count, 3)

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/integrations/email/limit",
            headers={"Authorization": "ApiKey api-key"},
            json=None,
            params=None,
            timeout=5,
        )
