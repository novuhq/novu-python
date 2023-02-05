"""This module is used to gather all DTO definitions related to the Event resource in Novu"""
import dataclasses

from novu.dto.base import CamelCaseDto
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
