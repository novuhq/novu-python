import types
from unittest import TestCase, mock

import pkg_resources

from novu.api import OrganizationApi
from novu.config import NovuConfig
from novu.dto import (
    MemberDto,
    MemberInviteDto,
    MemberUserDto,
    OrganizationBrandingDto,
    OrganizationDto,
    PartnerConfigurationDto,
)
from novu.enums import PartnerTypeEnum
from tests.factories import MockResponse

__version__ = pkg_resources.get_distribution("novu").version


class OrganizationApiTests(TestCase):
    api: OrganizationApi

    response_branding_json = {
        "logo": "https://s3-sample.com/logo.png",
        "color": "#f47373",
        "font_family": "inherit",
    }
    expected_branding_dto = OrganizationBrandingDto(
        logo="https://s3-sample.com/logo.png",
        color="#f47373",
        font_color=None,
        content_background=None,
        direction=None,
        font_family="inherit",
    )

    response_json = {
        "name": "Organization sample",
        "branding": response_branding_json,
        "partner_configurations": [
            {
                "access_token": "sample-access-token",
                "configuration_id": "63e969fcb6729e21337e2360",
                "partner_type": "vercel",
            }
        ],
    }
    expected_dto = OrganizationDto(
        name="Organization sample",
        branding=expected_branding_dto,
        partner_configurations=[
            PartnerConfigurationDto(
                access_token="sample-access-token",  # nosec
                configuration_id="63e969fcb6729e21337e2360",
                partner_type=PartnerTypeEnum.VERCEL,
            )
        ],
        logo=None,
    )

    response_member_json = {
        "_id": "64f0688bdd99c21f1e30a337",
        "_organization_id": "64f0638825339d16c5d2738a",
        "user": {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@email.com",
            "_id": "63e969fcb6729e21337e2360",
        },
        "roles": ["admin"],
        "invite": {
            "email": "john.doe@admin.fr",
            "token": "7bb26390-47e7-11ee-8f3b-7b63badb86ff",  # nosec
            "invitation_date": "2023-08-31T10:16:43.373Z",
        },
        "member_status": "invited",
    }
    expected_member_dto = MemberDto(
        _id="64f0688bdd99c21f1e30a337",
        _user_id=None,
        _organization_id="64f0638825339d16c5d2738a",
        user=MemberUserDto(
            first_name="John", last_name="Doe", email="john.doe@email.com", _id="63e969fcb6729e21337e2360"
        ),
        roles=["admin"],
        invite=MemberInviteDto(
            email="john.doe@admin.fr",
            token="7bb26390-47e7-11ee-8f3b-7b63badb86ff",  # nosec
            invitation_date="2023-08-31T10:16:43.373Z",
            answer_date=None,
            _invite_id=None,
        ),
        member_status="invited",
    )

    @classmethod
    def setUpClass(cls) -> None:
        NovuConfig.configure("sample.novu.com", "api-key")
        cls.api = OrganizationApi()

    @mock.patch("requests.request")
    def test_list_organizations(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, {"data": [self.response_json]})

        res = self.api.list()
        self.assertIsInstance(res, types.GeneratorType)
        self.assertEqual(list(res), [self.expected_dto])

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/organizations",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_create_organization_with_logo(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(201, {"data": self.response_json})

        # FIXME: Set a real-world test for logo data
        res = self.api.create(name="TEST", logo="unknown payload")
        self.assertIsInstance(res, OrganizationDto)
        self.assertEqual(res, self.expected_dto)

        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/organizations",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json={"name": "TEST", "logo": "unknown payload"},
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_create_organization_without_logo(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(201, {"data": self.response_json})

        res = self.api.create(name="TEST")
        self.assertIsInstance(res, OrganizationDto)
        self.assertEqual(res, self.expected_dto)

        mock_request.assert_called_once_with(
            method="POST",
            url="sample.novu.com/v1/organizations",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json={"name": "TEST"},
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_get_current(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, {"data": self.response_json})

        res = self.api.current()
        self.assertIsInstance(res, OrganizationDto)
        self.assertEqual(res, self.expected_dto)

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/organizations/me",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_rename(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, {"data": self.response_json})

        res = self.api.rename("new-name")
        self.assertIsNone(res)

        mock_request.assert_called_once_with(
            method="PATCH",
            url="sample.novu.com/v1/organizations",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json={"name": "new-name"},
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_list_members(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, {"data": [self.response_member_json]})

        res = self.api.list_members()
        self.assertIsInstance(res, types.GeneratorType)
        self.assertEqual(list(res), [self.expected_member_dto])

        mock_request.assert_called_once_with(
            method="GET",
            url="sample.novu.com/v1/organizations/members",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_remove_members(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, {"data": self.response_member_json})

        res = self.api.remove_member("64f0688bdd99c21f1e30a337")
        self.assertIsInstance(res, MemberDto)
        self.assertEqual(res, self.expected_member_dto)

        mock_request.assert_called_once_with(
            method="DELETE",
            url="sample.novu.com/v1/organizations/members/64f0688bdd99c21f1e30a337",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json=None,
            params=None,
            timeout=5,
        )

    @mock.patch("requests.request")
    def test_update_branding(self, mock_request: mock.MagicMock) -> None:
        mock_request.return_value = MockResponse(200, {"data": self.response_branding_json})

        res = self.api.update_branding(self.expected_branding_dto)
        self.assertIsInstance(res, OrganizationBrandingDto)
        self.assertEqual(res, self.expected_branding_dto)

        mock_request.assert_called_once_with(
            method="PUT",
            url="sample.novu.com/v1/organizations/branding",
            headers={"Authorization": "ApiKey api-key", "User-Agent": f"novu/python@{__version__}"},
            json={
                "logo": "https://s3-sample.com/logo.png",
                "color": "#f47373",
                "fontColor": None,
                "contentBackground": None,
                "direction": None,
                "fontFamily": "inherit",
            },
            params=None,
            timeout=5,
        )
