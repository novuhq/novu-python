"""This module is used to gather all DTO definitions related to the Topic resource in Novu"""
import dataclasses
from typing import List, Optional

from novu.dto.base import CamelCaseDto, DtoIterableDescriptor


@dataclasses.dataclass
class TriggerTopicDto(CamelCaseDto["TriggerTopicDto"]):
    """Topic definition for trigger"""

    topic_key: str
    type: str


@dataclasses.dataclass
class TopicDto(CamelCaseDto["TopicDto"]):
    """Topic definition"""

    camel_case_fields = ["key", "name"]
    # Actually, only these fields are editable in Novu, so prevent any activity on others

    key: str
    name: Optional[str] = None
    """Name, required during creation"""

    _id: Optional[str] = None
    """Topic ID in Novu internal system"""

    _organization_id: Optional[str] = None
    """Organization ID in Novu internal storage system"""

    _environment_id: Optional[str] = None
    """Environment ID in Novu internal storage system"""

    subscribers: Optional[List[str]] = None
    """List of subscribers in the topic."""


@dataclasses.dataclass
class PaginatedTopicDto(CamelCaseDto["PaginatedTopicDto"]):
    """Paginated topic definition"""

    page: int = 0
    total_count: int = 0
    page_size: int = 0
    data: DtoIterableDescriptor[TopicDto] = DtoIterableDescriptor[TopicDto](default_factory=list, item_cls=TopicDto)
