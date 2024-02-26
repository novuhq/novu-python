"""This module is used to gather all DTO definitions related to the Feed resource in Novu"""

import dataclasses
from typing import Optional

from novu.dto.base import CamelCaseDto


@dataclasses.dataclass
class FeedDto(CamelCaseDto["FeedDto"]):  # pylint: disable=R0902
    """Definition of a feed"""

    name: str
    """Name of the feed"""

    identifier: Optional[str] = None
    """Feed identifier, should be the given name set by default in Novu"""

    _id: Optional[str] = None
    """Feed ID in Novu internal storage system"""

    _environment_id: Optional[str] = None
    """Environment ID in Novu internal storage system"""

    _organization_id: Optional[str] = None
    """Organization ID in Novu internal storage system"""

    deleted: Optional[bool] = None
    """If the field is deleted"""

    created_at: Optional[str] = None
    """Creation date of the field"""

    updated_at: Optional[str] = None
    """Last update date of the feed"""

    id: Optional[str] = None  # pylint: disable=C0103
    """Feed ID in Novu internal storage system"""
