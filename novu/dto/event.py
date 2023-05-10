"""This module is used to gather all DTO definitions related to the Event resource in Novu"""
import dataclasses
from typing import List, Optional, Union

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


@dataclasses.dataclass
class InputEventDto(CamelCaseDto["InputEventDto"]):
    """Definition of an event used as an input"""

    name: str
    """The name of the template trigger to activate."""

    recipients: Union[str, List[str]]
    """A subscriber ID (or a list of subscriber ID) to reach with this trigger."""

    payload: dict
    """A JSON serializable python dict to pass additional custom information."""

    overrides: Optional[dict] = None
    """A JSON serializable python dict used to override provider specific configurations."""

    transaction_id: Optional[str] = None
    """A unique ID for this transaction."""

    actor: Optional[str] = None
    """It is used to display the Avatar of the provided actor's subscriber id."""
