"""This module is used to gather all DTO definitions related to the Layout resource in Novu"""
import dataclasses
from typing import Optional

from novu.dto.base import CamelCaseDto, DtoIterableDescriptor
from novu.enums import Channel, TemplateVariableTypeEnum


@dataclasses.dataclass
class LayoutVariableDto(CamelCaseDto["LayoutVariableDto"]):
    """Layout variable definition"""

    name: str
    """Layout variable name"""

    type: TemplateVariableTypeEnum
    """Layout variable type"""

    _id: Optional[str] = None
    """Layout variable ID in the Novu storage system"""

    required: bool = False
    """If this variable is required in layout"""

    default_value: Optional[str] = None
    """The variable default value in layout"""


@dataclasses.dataclass
class LayoutDto(CamelCaseDto["LayoutDto"]):  # pylint: disable=R0902
    """Layout definition"""

    camel_case_fields = ["name", "description", "content", "variables", "is_default"]
    # Actually, only these fields are editable in Novu, so prevent any activity on others

    name: str
    """Layout name"""

    description: str
    """Layout description"""

    content: str
    """Layout content, must contains at least {{{body}}}}"""

    is_default: bool
    """Layout is the default layout in your environment"""

    variables: DtoIterableDescriptor[LayoutVariableDto] = DtoIterableDescriptor[LayoutVariableDto](
        default_factory=list, item_cls=LayoutVariableDto
    )
    """List of variables used in the layout"""

    _id: Optional[str] = None
    """Layout ID in Novu internal storage system"""

    _environment_id: Optional[str] = None
    """Environment ID in Novu internal storage system"""

    _organization_id: Optional[str] = None
    """Organization ID in Novu internal storage system"""

    _creator_id: Optional[str] = None
    """Creator ID in Novu internal storage system"""

    content_type: Optional[str] = None
    """Content type of the layout"""

    channel: Optional[Channel] = None
    """Channel of the layout"""

    created_at: Optional[str] = None
    """Creation date-time of the layout"""

    updated_at: Optional[str] = None
    """Last date-time when the layout was updated"""

    is_deleted: Optional[bool] = None
    """If the layout is deleted"""


@dataclasses.dataclass
class PaginatedLayoutDto(CamelCaseDto["PaginatedLayoutDto"]):
    """Paginated layout definition"""

    page: int = 0
    """Page number"""

    total_count: int = 0
    """Total count"""

    page_size: int = 0
    """Page size"""

    data: DtoIterableDescriptor[LayoutDto] = DtoIterableDescriptor[LayoutDto](default_factory=list, item_cls=LayoutDto)
    """Data"""
