"""This module is used to gather all DTO definitions related to the Notification Template resource in Novu"""

import dataclasses
from typing import List, Optional

from novu.dto.base import CamelCaseDto, DtoDescriptor, DtoIterableDescriptor
from novu.dto.notification_group import NotificationGroupDto
from novu.dto.step_filter import StepFilterDto
from novu.dto.subscriber import SubscriberPreferenceChannelDto
from novu.enums.notification import (
    NotificationStepMetadataType,
    NotificationStepMetadataUnit,
)


@dataclasses.dataclass
class NotificationStepMetadataDto(CamelCaseDto["NotificationStepMetadataDto"]):
    """Definition of metadata for a notification step"""

    type: NotificationStepMetadataType
    """Define the kind of metadata (regular, backoff or scheduled)"""

    amount: Optional[int] = None
    """The amount of the notification step metadata"""

    unit: Optional[NotificationStepMetadataUnit] = None
    """The unit of the notification step metadata"""

    digest_key: Optional[str] = None
    """If specified, the digest engine will group the events based on the digestKey and subscriberId,
    otherwise the digest engine will group the events based only on the subscriberId.

    The digest key might come useful when you want a particular subscriber to get events grouped on a
    custom field. For example when an actor likes the user's post, you might want to digest based on the post_id key.
    """

    delay_path: Optional[str] = None
    """Payload path will determine the path in payload for the scheduled date.

    That path must be included in your payload on trigger execution and must be a date in strict ISO format.
    """

    backoff_unit: Optional[NotificationStepMetadataUnit] = None
    """The backoff unit of the notification step metadata"""

    update_mode: Optional[bool] = None
    """The update mode of the notification step metadata"""


@dataclasses.dataclass
class NotificationStepDto(CamelCaseDto["NotificationStepDto"]):  # pylint: disable=R0902
    """Definition of a notification step"""

    _id: Optional[str] = None
    """Notification Step ID in Novu internal storage system"""

    _template_id: Optional[str] = None
    """Notification Template ID in Novu internal storage system"""

    _parent_id: Optional[str] = None
    """Notification Step ID in Novu internal storage system (parent of this step)"""

    active: Optional[bool] = None
    """If this step is active"""

    should_stop_on_fail: Optional[bool] = None
    """The flow should stop the flow if this step fail ?"""

    template: Optional[dict] = None
    """Message template of the step"""

    filters: DtoIterableDescriptor[StepFilterDto] = DtoIterableDescriptor[StepFilterDto](
        default_factory=list, item_cls=StepFilterDto
    )
    """Filters of this template"""

    metadata: Optional[NotificationStepMetadataDto] = None
    """Metadata of this notification step"""

    replay_callback: Optional[dict] = None
    """Definition of the replay callback"""


@dataclasses.dataclass
class NotificationTriggerVariableDto(CamelCaseDto["NotificationTriggerVariableDto"]):
    """Definition of a trigger's variable for notification template"""

    name: str
    """Notification trigger variable's name"""


@dataclasses.dataclass
class NotificationTriggerDto(CamelCaseDto["NotificationTriggerDto"]):
    """Definition of a trigger for a notification template"""

    type: str
    """Notification trigger's type"""

    identifier: str
    """Notification trigger's identifier"""

    variables: DtoIterableDescriptor[NotificationTriggerVariableDto] = DtoIterableDescriptor[
        NotificationTriggerVariableDto
    ](default_factory=list, item_cls=NotificationTriggerVariableDto)
    """Variables of a notification trigger"""

    subscriber_variables: DtoIterableDescriptor[NotificationTriggerVariableDto] = DtoIterableDescriptor[
        NotificationTriggerVariableDto
    ](default_factory=list, item_cls=NotificationTriggerVariableDto)
    """Subscriber's variables of a notification trigger"""


@dataclasses.dataclass
class NotificationTemplateFormDto(CamelCaseDto["NotificationTemplateDto"]):  # pylint: disable=R0902
    """Definition of a notification template form (create / update)"""

    name: str
    """Name of the template"""

    notification_group_id: str
    """Notification Group ID from Novu internal storage system"""

    description: Optional[str] = None
    """A description of the template"""

    tags: Optional[List[str]] = None
    """Notification template's tags"""

    steps: DtoIterableDescriptor[NotificationStepDto] = DtoIterableDescriptor[NotificationStepDto](
        default_factory=list, item_cls=NotificationStepDto
    )
    """Steps of the template, which describe a step of your notification flow"""

    active: Optional[bool] = None
    """If the template is active"""

    critical: Optional[bool] = None
    """If the template should bypass user preferences"""

    draft: Optional[bool] = None
    """If the template is a draft"""

    preference_settings: Optional[DtoDescriptor[SubscriberPreferenceChannelDto]] = DtoDescriptor[
        SubscriberPreferenceChannelDto
    ](item_cls=SubscriberPreferenceChannelDto)
    """Preference settings of the notification template"""


@dataclasses.dataclass
class NotificationTemplateDto(CamelCaseDto["NotificationTemplateDto"]):  # pylint: disable=R0902
    """Definition of a notification template"""

    name: str
    """Name of the template"""

    description: Optional[str] = None
    """A description of the template"""

    tags: Optional[List[str]] = None
    """Notification template's tags"""

    steps: DtoIterableDescriptor[NotificationStepDto] = DtoIterableDescriptor[NotificationStepDto](
        default_factory=list, item_cls=NotificationStepDto
    )
    """Steps of the template, which describe a step of your notification flow"""

    active: Optional[bool] = None
    """If the template is active"""

    critical: Optional[bool] = None
    """If the template should bypass user preferences"""

    draft: Optional[bool] = None
    """If the template is a draft"""

    preference_settings: Optional[DtoDescriptor[SubscriberPreferenceChannelDto]] = DtoDescriptor[
        SubscriberPreferenceChannelDto
    ](item_cls=SubscriberPreferenceChannelDto)
    """Preference settings of the notification template"""

    triggers: DtoIterableDescriptor[NotificationTriggerDto] = DtoIterableDescriptor[NotificationTriggerDto](
        default_factory=list, item_cls=NotificationTriggerDto
    )
    """Usable triggers to launch this notification template"""

    _id: Optional[str] = None
    """Notification Template ID in Novu internal storage system"""

    _environment_id: Optional[str] = None
    """Environment ID in Novu internal storage system"""

    _organization_id: Optional[str] = None
    """Organization ID in Novu internal storage system"""

    _notification_group_id: Optional[str] = None
    """Notification Group ID in Novu internal storage system"""

    _parent_id: Optional[str] = None
    """Parent ID in Novu internal storage system"""

    _creator_id: Optional[str] = None
    """Creator ID in Novu internal storage system"""

    notification_group: Optional[DtoDescriptor[NotificationGroupDto]] = DtoDescriptor[NotificationGroupDto](
        item_cls=NotificationGroupDto
    )
    """Notification group linked to the notification template"""

    created_at: Optional[str] = None
    """The notification template's creation date"""

    updated_at: Optional[str] = None
    """The last notification template's update date"""

    deleted_at: Optional[str] = None
    """The notification template has been deleted at"""

    deleted: Optional[bool] = None
    """If the notification template is deleted"""


@dataclasses.dataclass
class PaginatedNotificationTemplateDto(CamelCaseDto["PaginatedNotificationTemplateDto"]):
    """Definition of paginated subscribers"""

    page: int = 0
    """Page number"""

    total_count: int = 0
    """Total count"""

    page_size: int = 0
    """Page size"""

    data: DtoIterableDescriptor[NotificationTemplateDto] = DtoIterableDescriptor[NotificationTemplateDto](
        default_factory=list, item_cls=NotificationTemplateDto
    )
    """Data"""
