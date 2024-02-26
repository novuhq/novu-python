"""This module is used to gather all DTO definitions related to the Integration resource in Novu"""

import dataclasses
from typing import Dict, Optional, Union

from novu.dto.base import CamelCaseDto
from novu.enums import Channel, CredentialsKeyEnum, ProviderIdEnum


@dataclasses.dataclass
class IntegrationDto(CamelCaseDto["IntegrationDto"]):  # pylint: disable=R0902
    """Definition of an integration"""

    camel_case_fields = ["provider_id", "channel", "credentials", "active"]
    # Actually, only these fields are editable in Novu, so prevent any activity on others

    provider_id: ProviderIdEnum
    """Provider ID, which is one of predefined available enum"""

    channel: Channel
    """Integration channel"""

    active: bool
    """If the provider is active"""

    credentials: Optional[Dict[CredentialsKeyEnum, Union[str, bool]]] = None
    """Credentials of the provider"""

    _id: Optional[str] = None
    """Integration ID in Novu internal storage system"""

    _environment_id: Optional[str] = None
    """Environment ID in Novu internal storage system"""

    _organization_id: Optional[str] = None
    """Organization ID in Novu internal storage system"""

    created_at: Optional[str] = None
    """Date-time of the integration initial configuration"""

    updated_at: Optional[str] = None
    """Date-time of the last update of the integration"""

    deleted_at: Optional[str] = None
    """Date-time of the removal of the integration"""

    deleted_by: Optional[str] = None
    """User how ask for the removal of the integration"""

    deleted: Optional[bool] = None
    """If the integration is deleted"""


@dataclasses.dataclass
class IntegrationChannelUsageDto(CamelCaseDto["IntegrationChannelUsageDto"]):
    """Definition of an integration usage (scoped to a channel)"""

    count: Optional[int]
    """Usage count of the channel"""

    limit: Optional[int]
    """Usage limit of the channel"""
