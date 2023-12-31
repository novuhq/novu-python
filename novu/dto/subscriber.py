"""This module is used to gather all DTO definitions related to the Subscriber resource in Novu"""
import dataclasses
from typing import List, Optional

from novu.dto.base import CamelCaseDto, DtoDescriptor, DtoIterableDescriptor
from novu.enums.provider import ProviderIdEnum


@dataclasses.dataclass
class SubscriberPreferenceChannelDto(CamelCaseDto["SubscriberPreferenceChannelDto"]):
    """Definition of a channel activation state in subscriber's preference"""

    email: Optional[bool] = True
    """Email notification activated?"""

    sms: Optional[bool] = True
    """SMS notification activated?"""

    in_app: Optional[bool] = True  # FIXME: Find a way to not camelize this field
    """In APP notification activated?"""

    chat: Optional[bool] = True
    """Chat notification activated?"""

    push: Optional[bool] = True
    """Push notification activated?"""


@dataclasses.dataclass
class SubscriberPreferenceTemplateDto(CamelCaseDto["SubscriberPreferenceTemplateDto"]):
    """Definition of a template in subscriber's preference"""

    _id: Optional[str] = None
    """Subscriber preference template's ID"""

    name: Optional[str] = None
    """Name of the subscriber's preference template"""

    critical: Optional[bool] = None
    """Defines if the user's preferences will be ignored or not by Novu for the given template.

    By defining the template as critical, Novu considers that all steps should be executed ignoring user preferences.
    """


@dataclasses.dataclass
class SubscriberPreferencePreferenceDto(CamelCaseDto["SubscriberPreferencePreferenceDto"]):
    """Definition of subscriber's preference sub-struct"""

    enabled: bool
    """If the subscriber preference are enabled"""

    channels: DtoDescriptor[SubscriberPreferenceChannelDto] = DtoDescriptor[SubscriberPreferenceChannelDto](
        item_cls=SubscriberPreferenceChannelDto
    )
    """The activation states of the different channels"""


@dataclasses.dataclass
class SubscriberPreferenceDto(CamelCaseDto["SubscriberPreferenceDto"]):
    """Definition of subscriber's preference"""

    preference: DtoDescriptor[SubscriberPreferencePreferenceDto] = DtoDescriptor[SubscriberPreferencePreferenceDto](
        item_cls=SubscriberPreferencePreferenceDto
    )
    """Sub-struct in Novu for preference / global activation state"""

    template: DtoDescriptor[SubscriberPreferenceTemplateDto] = DtoDescriptor[SubscriberPreferenceTemplateDto](
        item_cls=SubscriberPreferenceTemplateDto
    )
    """The identifiers of the template linked to the preferences and its criticality"""


@dataclasses.dataclass
class SubscriberChannelSettingsCredentialsDto(CamelCaseDto["SubscriberChannelSettingsCredentialsDto"]):
    """Credentials payload for the specified provider."""

    webhook_url: Optional[str] = None
    """Webhook url used by chat app integrations. The webhook should be obtained from the chat app provider"""

    channel: Optional[str] = None
    """Channel specification for Mattermost chat notifications"""

    device_tokens: Optional[List[str]] = None
    """Contains an array of the subscriber device tokens for a given provider. Used on Push integrations"""


@dataclasses.dataclass
class SubscriberChannelSettingsDto(CamelCaseDto["SubscriberChannelSettingsDto"]):
    """Definition of channel settings for subscriber."""

    provider_id: ProviderIdEnum
    """The provider identifier for the credentials"""

    _integration_id: str
    """Id of the integration that is used for this channel"""

    credentials: DtoDescriptor[SubscriberChannelSettingsCredentialsDto] = DtoDescriptor[
        SubscriberChannelSettingsCredentialsDto
    ](item_cls=SubscriberChannelSettingsCredentialsDto)
    """Credentials of this channel"""

    integration_identifier: Optional[str] = None
    """The integration identifier"""


@dataclasses.dataclass
class SubscriberDto(CamelCaseDto["SubscriberDto"]):  # pylint: disable=R0902
    """Definition of subscriber"""

    camel_case_fields = [
        "subscriber_id",
        "email",
        "first_name",
        "last_name",
        "phone",
        "avatar",
        "locale",
        "channels",
        "data",
    ]
    # Actually, only these fields are editable in Novu, so prevent any activity on others

    subscriber_id: str
    """Subscriber's ID"""

    email: Optional[str] = None
    """Email of the subscriber"""

    first_name: Optional[str] = None
    """First name of the subscriber"""

    last_name: Optional[str] = None
    """Last name of the subscriber"""

    phone: Optional[str] = None
    """Phone number of the subscriber"""

    avatar: Optional[str] = None
    """profile picture (must be a public url to access the avatar)"""

    locale: Optional[str] = None
    """language code (we recommend the use of ISO 639 to define them)"""

    _id: Optional[str] = None
    """Subscriber ID in Novu internal storage system"""

    _environment_id: Optional[str] = None
    """Environment ID in Novu internal storage system"""

    _organization_id: Optional[str] = None
    """Organization ID in Novu internal storage system"""

    channels: DtoIterableDescriptor[SubscriberChannelSettingsDto] = DtoIterableDescriptor[SubscriberChannelSettingsDto](
        default_factory=list, item_cls=SubscriberChannelSettingsDto
    )
    """Subscriber provider specific credentials"""

    deleted: Optional[bool] = None
    """If the subscriber is deleted"""

    created_at: Optional[str] = None
    """Creation date of the subscriber"""

    updated_at: Optional[str] = None
    """Last update date of the subscriber"""

    is_online: Optional[bool] = None
    """If the subscriber is online"""

    last_online_at: Optional[str] = None
    """Last connection date of the subscriber"""

    data: Optional[dict] = None
    """Apart from the above fixed structured user data, this field contain
    any unstructured custom data such as user’s address, nationality, height, etc."""


@dataclasses.dataclass
class PaginatedSubscriberDto(CamelCaseDto["PaginatedSubscriberDto"]):
    """Definition of paginated subscribers"""

    page: int = 0
    """Page number"""

    total_count: int = 0
    """Total count"""

    page_size: int = 0
    """Page size"""

    data: DtoIterableDescriptor[SubscriberDto] = DtoIterableDescriptor[SubscriberDto](
        default_factory=list, item_cls=SubscriberDto
    )
    """Data"""


@dataclasses.dataclass
class BulkResultSubscriberDto(CamelCaseDto["BulkResultSubscriberDto"]):
    """Definition of paginated subscribers"""

    created: DtoIterableDescriptor[SubscriberDto] = DtoIterableDescriptor[SubscriberDto](
        default_factory=list, item_cls=SubscriberDto
    )
    """List of subscribers that were created during the operation."""

    updated: DtoIterableDescriptor[SubscriberDto] = DtoIterableDescriptor[SubscriberDto](
        default_factory=list, item_cls=SubscriberDto
    )
    """List of subscribers that were updated during the operation."""

    failed: DtoIterableDescriptor[SubscriberDto] = DtoIterableDescriptor[SubscriberDto](
        default_factory=list, item_cls=SubscriberDto
    )
    """List of subscribers whose creation (or update) failed."""
