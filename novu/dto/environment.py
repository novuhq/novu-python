"""This module is used to gather all DTO definitions related to the Environment resource in Novu"""

import dataclasses
from typing import Optional

from novu.dto.base import CamelCaseDto, DtoDescriptor, DtoIterableDescriptor


@dataclasses.dataclass
class EnvironmentWidgetDto(CamelCaseDto["EnvironmentWidgetDto"]):
    """Definition of an environment's widget"""

    notification_center_encryption: bool
    """If the notification center use encryption"""


@dataclasses.dataclass
class EnvironmentApiKeyDto(CamelCaseDto["EnvironmentApiKeyDto"]):
    """Definition of an environment's api-key"""

    key: str
    """The API key"""

    _user_id: str
    """The user identifier related to the api-key"""

    _id: Optional[str] = None
    """Environment's API Key ID in Novu internal storage system"""


@dataclasses.dataclass
class EnvironmentDto(CamelCaseDto["EnvironmentDto"]):  # pylint: disable=R0902
    """Definition of an environment"""

    id: Optional[str] = None  # pylint: disable=C0103
    """Environment ID in Novu internal storage system"""

    _id: Optional[str] = None
    """Environment ID in Novu internal storage system"""

    name: Optional[str] = None
    """Name of the environment"""

    identifier: Optional[str] = None
    """Identifier of the environment"""

    _organization_id: Optional[str] = None
    """Organization ID in Novu internal storage system"""

    widget: DtoDescriptor[EnvironmentWidgetDto] = DtoDescriptor[EnvironmentWidgetDto](item_cls=EnvironmentWidgetDto)
    """Environment's widget settings"""

    api_keys: DtoIterableDescriptor[EnvironmentApiKeyDto] = DtoIterableDescriptor[EnvironmentApiKeyDto](
        default_factory=list, item_cls=EnvironmentApiKeyDto
    )
    """List of API Keys related to the environment"""

    created_at: Optional[str] = None
    """Creation date of the environment"""

    updated_at: Optional[str] = None
    """Last update date of the environment"""
