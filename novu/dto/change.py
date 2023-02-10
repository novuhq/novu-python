"""This module is used to gather all DTO definitions related to the Change resource in Novu"""
import dataclasses
from typing import Any, List, Optional

from novu.dto.base import CamelCaseDto, DtoIterableDescriptor
from novu.enums import ChangeKind


@dataclasses.dataclass
class ChangeDetailDto(CamelCaseDto["ChangeDetailDto"]):
    """Definition of a change detail"""

    op: Optional[str] = None  # pylint: disable=C0103
    """The operation code of the change"""

    path: Optional[List[str]] = None
    """The path of the modification"""

    val: Optional[Any] = None
    """Value of the change, struct depend of the context"""


@dataclasses.dataclass
class ChangeDto(CamelCaseDto["ChangeDto"]):  # pylint: disable=R0902
    """Definition of a change"""

    _id: Optional[str] = None
    """Change ID in Novu internal storage system"""

    _environment_id: Optional[str] = None
    """Environment ID in Novu internal storage system"""

    _organization_id: Optional[str] = None
    """Organization ID in Novu internal storage system"""

    _entity_id: Optional[str] = None
    """Entity ID in Novu internal storage system"""

    _parent_id: Optional[str] = None
    """Parent ID in Novu internal storage system"""

    enabled: Optional[bool] = None
    """If the change was enabled."""

    type: Optional[ChangeKind] = None
    """Kind of change applied."""

    change: DtoIterableDescriptor[ChangeDetailDto] = DtoIterableDescriptor[ChangeDetailDto](
        default_factory=list, item_cls=ChangeDetailDto
    )
    """Details about a change"""

    created_at: Optional[str] = None
    """Date-time of the integration initial configuration"""

    updated_at: Optional[str] = None
    """Date-time of the last update of the integration"""


@dataclasses.dataclass
class PaginatedChangeDto(CamelCaseDto["PaginatedChangeDto"]):
    """Definition of paginated changes"""

    page: int = 0
    total_count: int = 0
    page_size: int = 0
    data: DtoIterableDescriptor[ChangeDto] = DtoIterableDescriptor[ChangeDto](default_factory=list, item_cls=ChangeDto)
