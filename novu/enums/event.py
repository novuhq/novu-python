"""This module is used to gather enumerations related to the Event resource in Novu"""
from enum import Enum


class EventStatus(Enum):
    """This enumeration define possible status of an event"""

    PROCESSED = "processed"
    """The event have been processed"""

    TRIGGER_NOT_ACTIVE = "trigger_not_active"
    """The trigger you gave is not active"""

    TEMPLATE_NOT_FOUND = "template_not_found"
    """The template was not found"""

    SUBSCRIBER_ID_MISSING = "subscriber_id_missing"
    """The subscriber ID you gave was not found"""
