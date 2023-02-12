"""This module is used to gather all python wrappers used to describe resources in Novu API.

In this SDK, we choose to split the Novu API by business resource to simplify its complexity.
"""
from novu.api.change import ChangeApi
from novu.api.event import EventApi
from novu.api.feed import FeedApi
from novu.api.integration import IntegrationApi
from novu.api.layout import LayoutApi
from novu.api.notification_group import NotificationGroupApi
from novu.api.notification_template import NotificationTemplateApi
from novu.api.subscriber import SubscriberApi
from novu.api.topic import TopicApi

__all__ = [
    "ChangeApi",
    "EventApi",
    "FeedApi",
    "IntegrationApi",
    "LayoutApi",
    "NotificationGroupApi",
    "NotificationTemplateApi",
    "SubscriberApi",
    "TopicApi",
]
