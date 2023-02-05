"""This module is used to gather all Data Transfer Object definitions in the Novu SDK.

All definitions of format returned by the Novu API are here, which help us to instantiate and document them
for developer purpose (instead of getting raw dict without any hint about what is in it).
"""

from novu.dto.event import EventDto
from novu.dto.integration import IntegrationChannelUsageDto, IntegrationDto
from novu.dto.layout import LayoutDto, LayoutVariableDto, PaginatedLayoutDto
from novu.dto.subscriber import (
    PaginatedSubscriberDto,
    SubscriberDto,
    SubscriberPreferenceChannelDto,
    SubscriberPreferenceDto,
    SubscriberPreferencePreferenceDto,
    SubscriberPreferenceTemplateDto,
)
from novu.dto.topic import PaginatedTopicDto, TopicDto, TriggerTopicDto

__all__ = [
    "EventDto",
    "IntegrationDto",
    "IntegrationChannelUsageDto",
    "LayoutDto",
    "LayoutVariableDto",
    "PaginatedLayoutDto",
    "PaginatedSubscriberDto",
    "SubscriberDto",
    "SubscriberPreferenceChannelDto",
    "SubscriberPreferenceDto",
    "SubscriberPreferencePreferenceDto",
    "SubscriberPreferenceTemplateDto",
    "PaginatedTopicDto",
    "TopicDto",
    "TriggerTopicDto",
]
