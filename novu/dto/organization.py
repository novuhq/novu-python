"""This module is used to gather all DTO definitions related to the Organization resource in Novu.

An organization serves as a separate entity within your Novu account.
Each organization you create has its own separate integration store, workflows, subscribers, and API keys.
This separation of resources allows you to manage multi-tenant environments and
separate domains within a single account.
"""

import dataclasses
from typing import List, Optional

from novu.dto.base import CamelCaseDto, DtoDescriptor, DtoIterableDescriptor
from novu.enums import OrganizationBrandingDirection, PartnerTypeEnum


@dataclasses.dataclass
class PartnerConfigurationDto(CamelCaseDto["PartnerConfigurationDto"]):
    """Organization partner configuration definition"""

    access_token: str
    """Access token"""

    configuration_id: str
    """Configuration identifier"""

    partner_type: PartnerTypeEnum
    """Partner type"""

    team_id: Optional[str] = None
    """Partner team identifier"""

    project_ids: Optional[List[str]] = None
    """Partner's project identifiers"""


@dataclasses.dataclass
class OrganizationBrandingDto(CamelCaseDto["OrganizationBrandingDto"]):
    """Organization branding definition"""

    logo: Optional[str] = None
    """Branding logo"""

    color: Optional[str] = None
    """Branding color"""

    font_color: Optional[str] = None
    """Branding font color"""

    content_background: Optional[str] = None
    """Branding background content"""

    direction: Optional[OrganizationBrandingDirection] = None
    """Branding direction"""

    font_family: Optional[str] = None
    """Branding font-family"""


@dataclasses.dataclass
class OrganizationDto(CamelCaseDto["OrganizationDto"]):  # pylint: disable=R0902
    """Organization definition"""

    name: str
    """Organization name"""

    branding: DtoDescriptor[OrganizationBrandingDto] = DtoDescriptor[OrganizationBrandingDto](
        item_cls=OrganizationBrandingDto
    )
    """Organization branding"""

    partner_configurations: DtoIterableDescriptor[PartnerConfigurationDto] = DtoIterableDescriptor[
        PartnerConfigurationDto
    ](default_factory=list, item_cls=PartnerConfigurationDto)
    """List of partner configurations used in the organization"""

    logo: Optional[str] = None
    """Organization's logo (S3 signed URL if you read information from API)"""
