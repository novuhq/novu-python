"""This module is used to gather enumerations related to the Change resource in Novu"""

from novu.enums.polyfill import StrEnum


class ChangeKind(StrEnum):
    """This enumeration define all kinds of change in Novu"""

    FEED = "Feed"
    """The change is related to a feed"""

    MESSAGE_TEMPLATE = "MessageTemplate"
    """The change is related to a message template"""

    LAYOUT = "Layout"
    """The change is related to a layout"""

    NOTIFICATION_TEMPLATE = "NotificationTemplate"
    """The change is related to a notification template"""

    NOTIFICATION_GROUP = "NotificationGroup"
    """The change is related to a notification group"""
