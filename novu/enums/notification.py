"""This module is used to gather enumerations related to the Notification resource in Novu"""
from enum import Enum


class NotificationStepMetadataType(Enum):
    """This enumeration define possible type of step's metadata"""

    REGULAR = "regular"
    BACKOFF = "backoff"
    SCHEDULED = "scheduled"


class NotificationStepMetadataUnit(Enum):
    """This enumeration define possible unit of step's metadata"""

    SECONDS = "seconds"
    MINUTES = "minutes"
    HOURS = "hours"
    DAYS = "days"
