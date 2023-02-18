"""This module is used to gather all DTO definitions related to the Step Filter resource in Novu"""
import dataclasses
from typing import Optional

from novu.dto.base import CamelCaseDto, DtoIterableDescriptor
from novu.dto.field import FieldFilterPartDto
from novu.enums.step_filter import StepFilterType, StepFilterValue


@dataclasses.dataclass
class StepFilterDto(CamelCaseDto["StepFilterDto"]):
    """Definition of a step filter"""

    is_negated: Optional[bool] = None
    """If the filter should be negated"""

    type: Optional[StepFilterType] = None
    """Step filter's type"""

    value: Optional[StepFilterValue] = None
    """Step filter's value"""

    children: DtoIterableDescriptor[FieldFilterPartDto] = DtoIterableDescriptor[FieldFilterPartDto](
        default_factory=list, item_cls=FieldFilterPartDto
    )
    """Step filter's children"""
