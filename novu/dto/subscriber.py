"""This module is used to gather all DTO definitions related to the Subscriber resource in Novu"""
import dataclasses
from typing import Optional

from novu.dto.base import CamelCaseDto, DtoDescriptor, DtoIterableDescriptor


@dataclasses.dataclass
class SubscriberPreferenceChannelDto(CamelCaseDto["SubscriberPreferenceChannelDto"]):
    """Definition of a channel activation state in subscriber's preference"""

    email: Optional[bool] = True
    sms: Optional[bool] = True
    in_app: Optional[bool] = True  # FIXME: Find a way to not camelize this field
    chat: Optional[bool] = True
    push: Optional[bool] = True


@dataclasses.dataclass
class SubscriberPreferenceTemplateDto(CamelCaseDto["SubscriberPreferenceTemplateDto"]):
    """Definition of a template in subscriber's preference"""

    _id: Optional[str] = None
    name: Optional[str] = None

    critical: Optional[bool] = None
    """Defines if the user's preferences will be ignored or not by Novu for the given template.

    By defining the template as critical, Novu considers that all steps should be executed ignoring user preferences.
    """


@dataclasses.dataclass
class SubscriberPreferencePreferenceDto(CamelCaseDto["SubscriberPreferencePreferenceDto"]):
    """Definition of subscriber's preference sub-struct"""

    enabled: bool
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
class SubscriberDto(CamelCaseDto["SubscriberDto"]):  # pylint: disable=R0902
    """Definition of subscriber"""

    camel_case_fields = ["subscriber_id", "email", "first_name", "last_name", "phone", "avatar", "locale"]
    # Actually, only these fields are editable in Novu, so prevent any activity on others

    subscriber_id: str
    email: str

    first_name: Optional[str] = None
    last_name: Optional[str] = None
    phone: Optional[str] = None

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

    # TODO: add channels
    deleted: Optional[bool] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    is_online: Optional[bool] = None
    last_online_at: Optional[str] = None


@dataclasses.dataclass
class PaginatedSubscriberDto(CamelCaseDto["PaginatedSubscriberDto"]):
    """Definition of paginated subscribers"""

    page: int = 0
    total_count: int = 0
    page_size: int = 0
    data: DtoIterableDescriptor[SubscriberDto] = DtoIterableDescriptor[SubscriberDto](
        default_factory=list, item_cls=SubscriberDto
    )
