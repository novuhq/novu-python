"""This module is used to gather all DTO definitions related to the Blueprint resource in Novu"""
import dataclasses
from typing import List, Optional

from novu.dto.base import CamelCaseDto, DtoIterableDescriptor


@dataclasses.dataclass
class BlueprintDto(CamelCaseDto["BlueprintDto"]):  # pylint: disable=R0902
    """Blueprint definition."""

    name: str
    """Blueprint name."""

    description: str
    """Blueprint description."""

    _id: Optional[str] = None
    """Blueprint ID in Novu internal storage system."""

    _environment_id: Optional[str] = None
    """Environment ID in Novu internal storage system."""

    _organization_id: Optional[str] = None
    """Organization ID in Novu internal storage system."""

    _notification_group_id: Optional[str] = None
    """Notification group ID in Novu internal storage system."""

    _creator_id: Optional[str] = None
    """Creator ID in Novu internal storage system."""

    created_at: Optional[str] = None
    """Creation date-time of the blueprint."""

    updated_at: Optional[str] = None
    """Last date-time when the blueprint was updated."""

    deleted: Optional[bool] = None
    """If the blueprint is deleted."""

    deleted_at: Optional[str] = None
    """Date-time of the removal of the blueprint."""

    deleted_by: Optional[str] = None
    """User who asked for the removal of the blueprint."""

    critical: Optional[bool] = None
    """If the blueprint is critical."""

    _parent_id: Optional[str] = None
    """Parent ID in Novu internal storage system."""

    active: Optional[bool] = None
    """Active status of the blueprint."""

    blueprint_id: Optional[str] = None
    """Blueprint ID in Novu internal storage system."""

    draft: Optional[bool] = None
    """Draft status of the blueprint."""

    is_blueprint: Optional[bool] = None
    """If the object is a blueprint."""

    notification_group: Optional[object] = None
    """Notification group object."""

    preference_settings: Optional[object] = None
    """Preference settings object."""

    steps: Optional[List[object]] = None
    """List of steps in the blueprint."""

    tags: Optional[List[str]] = None
    """List of tags associated with the blueprint."""

    triggers: Optional[List[object]] = None
    """List of triggers in the blueprint."""


@dataclasses.dataclass
class GroupedBlueprintDto(CamelCaseDto["GroupedBlueprintDto"]):
    """Grouped blueprint definition."""

    category: str
    """Blueprint category."""

    general: DtoIterableDescriptor[BlueprintDto] = DtoIterableDescriptor[BlueprintDto](
        default_factory=list, item_cls=BlueprintDto
    )
    """List of general blueprints in the category."""

    popular: DtoIterableDescriptor[BlueprintDto] = DtoIterableDescriptor[BlueprintDto](
        default_factory=list, item_cls=BlueprintDto
    )
    """List of popular blueprints in the category."""
