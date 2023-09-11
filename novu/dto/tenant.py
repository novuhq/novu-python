"""This module is used to gather all DTO definitions related to the Tenant resource in Novu"""
import dataclasses
from typing import Optional

from novu.dto.base import CamelCaseDto, DtoIterableDescriptor


@dataclasses.dataclass
class TenantDto(CamelCaseDto["TenantDto"]):
    """Tenant definition"""

    identifier: str
    """Tenant identifier"""

    name: str
    """Tenant name"""

    data: Optional[dict] = None
    """Unstructured dictionary of data stored on the tenant"""

    _id: Optional[str] = None
    """Topic ID in Novu internal system"""

    _environment_id: Optional[str] = None
    """Environment ID in Novu internal storage system"""

    created_at: Optional[str] = None
    """Creation date of the subscriber"""

    updated_at: Optional[str] = None
    """Last update date of the subscriber"""


@dataclasses.dataclass
class PaginatedTenantDto(CamelCaseDto["PaginatedTenantDto"]):
    """Paginated topic definition"""

    page: int = 0
    """Page number"""

    has_more: bool = False
    """Does the list have more items to fetch"""

    page_size: int = 0
    """Page size"""

    data: DtoIterableDescriptor[TenantDto] = DtoIterableDescriptor[TenantDto](default_factory=list, item_cls=TenantDto)
    """Data"""
