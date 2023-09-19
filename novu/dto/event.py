"""This module is used to gather all DTO definitions related to the Event resource in Novu"""
import dataclasses
from typing import List, Optional, Union

from novu.dto.base import CamelCaseDto, DtoDescriptor
from novu.enums import EventStatus


@dataclasses.dataclass
class EventDto(CamelCaseDto["EventDto"]):
    """Definition of an event"""

    acknowledged: bool
    """If trigger was acknowledged or not."""

    status: EventStatus
    """Status for trigger."""

    transaction_id: str
    """Transaction id for trigger."""


@dataclasses.dataclass
class RecipientDto(CamelCaseDto["RecipientDto"]):
    """The recipients list of people who will receive the notification."""

    subscriber_id: str
    """Subscriber ID of the recipient."""

    email: Optional[str] = None
    """Email of the recipient."""

    first_name: Optional[str] = None
    """First name of the recipient."""

    last_name: Optional[str] = None
    """Last name of the recipient."""

    phone: Optional[str] = None
    """Phone number of the recipient."""

    avatar: Optional[str] = None
    """Avatar URL of the recipient."""

    locale: Optional[str] = None
    """Locale(language and region) of the recipient, ."""

    data: Optional[dict] = None
    """Additional data for the recipient."""


@dataclasses.dataclass
class InputEventDto(CamelCaseDto["InputEventDto"]):
    """Definition of an event used as an input"""

    name: str
    """The name of the template trigger to activate."""

    payload: dict
    """A JSON serializable python dict to pass additional custom information."""

    recipients: DtoDescriptor[RecipientDto] = DtoDescriptor[RecipientDto](item_cls=RecipientDto)

    overrides: Optional[dict] = None
    """A JSON serializable python dict used to override provider specific configurations."""

    transaction_id: Optional[str] = None
    """A unique ID for this transaction."""

    actor: Optional[str] = None
    """It is used to display the Avatar of the provided actor's subscriber id."""
