"""This module is used to gather all DTO definitions related to the Message resource in Novu"""
import dataclasses
from typing import List, Optional

from novu.dto.base import CamelCaseDto, DtoIterableDescriptor
from novu.enums import Channel, ProviderIdEnum


@dataclasses.dataclass
class MessageDto(CamelCaseDto["MessageDto"]):  # pylint: disable=R0902
    """Definition of an event"""

    identifier: Optional[str] = None
    """The message identifier"""

    _id: Optional[str] = None
    """Message Notification ID in Novu internal storage system"""

    _template_id: Optional[str] = None
    """Template ID in Novu internal storage system"""

    _environment_id: Optional[str] = None
    """Environment ID in Novu internal storage system"""

    _message_template_id: Optional[str] = None
    """Message Template ID in Novu internal storage system"""

    _organization_id: Optional[str] = None
    """Organization ID in Novu internal storage system"""

    _subscriber_id: Optional[str] = None
    """Subscriber ID in Novu internal storage system"""

    _job_id: Optional[str] = None
    """Job ID in Novu internal storage system"""

    template_identifier: Optional[str] = None
    """Template ID in Novu internal storage system"""

    email: Optional[str] = None
    """Email of the subscriber triggered where the message has been sent"""

    subject: Optional[str] = None
    """Subject of the email sent"""

    cta: Optional[dict] = None
    """Definition of the call to action used on message"""

    channel: Optional[Channel] = None
    """Channel used for the message"""

    content: Optional[str] = None
    """Content of the message"""

    provider_id: Optional[ProviderIdEnum] = None
    """Provider ID used for the message"""

    device_tokens: Optional[List[dict]] = None
    """A list of device tokens used on the provider to send message"""

    seen: Optional[bool] = None
    """If the message has been seen."""

    read: Optional[bool] = None
    """If the message has been read"""

    status: Optional[str] = None
    """Status of the activity notification"""

    transaction_id: Optional[str] = None
    """Transaction ID in Novu internal storage system"""

    payload: Optional[dict] = None
    """Payload used during trigger"""

    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    deleted: Optional[bool] = None

    last_read_date: Optional[str] = None
    """Timestamp of the last read event registered"""

    last_seen_date: Optional[str] = None
    """Timestamp of the last seen event registered"""


@dataclasses.dataclass
class PaginatedMessageDto(CamelCaseDto["PaginatedMessageDto"]):
    """Paginated message definition"""

    page: int = 0
    total_count: int = 0
    page_size: int = 0
    data: DtoIterableDescriptor[MessageDto] = DtoIterableDescriptor[MessageDto](
        default_factory=list, item_cls=MessageDto
    )
