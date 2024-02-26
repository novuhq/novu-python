"""This module is used to gather enumerations related to the Message resource in Novu"""

from novu.enums.polyfill import StrEnum


class MarkAsEnum(StrEnum):
    """This enumeration define possible instruction for a mark-as instruction"""

    READ = "read"
    """Mark message as read"""

    SEEN = "seen"
    """Mark message as seen"""

    UNREAD = "unread"
    """Mark message as unread"""

    UNSEEN = "unseen"
    """Mark message as unseen"""


class MessageActionStatus(StrEnum):
    """This enumeration define possible message action status"""

    PENDING = "pending"
    """Message action status is pending"""

    DONE = "done"
    """Message action status is done"""
