"""This module is used to gather enumerations related to the Change resource in Novu"""
from enum import Enum


class ChangeKind(Enum):
    """This enumeration define all kinds of change in Novu"""

    FEED = "Feed"
    MESSAGE_TEMPLATE = "MessageTemplate"
    LAYOUT = "Layout"
    NOTIFICATION_TEMPLATE = "NotificationTemplate"
    NOTIFICATION_GROUP = "NotificationGroup"
