"""This module is used to gather enumerations related to the Notification resource in Novu"""
from enum import Enum


class NotificationStepMetadataType(Enum):
    """This enumeration define possible type of step's metadata"""

    REGULAR = "regular"
    """Metadata for a digest in regular mode"""

    BACKOFF = "backoff"
    """Metadata for a digest in back-off mode"""

    SCHEDULED = "scheduled"
    """Metadata for a scheduled step"""


class NotificationStepMetadataUnit(Enum):
    """This enumeration define possible unit of step's metadata"""

    SECONDS = "seconds"
    """In seconds"""

    MINUTES = "minutes"
    """In minutes"""

    HOURS = "hours"
    """In hours"""

    DAYS = "days"
    """In days"""
