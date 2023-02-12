"""This module is used to gather all DTO definitions related to the Event resource in Novu"""
import dataclasses

from novu.dto.base import CamelCaseDto
from novu.enums.field import FieldFilterPartOn, FieldFilterPartOperator


@dataclasses.dataclass
class FieldFilterPartDto(CamelCaseDto["FieldFilterPartDto"]):
    """Definition of a field filter part"""

    field: str
    value: str
    operator: FieldFilterPartOperator
    on: FieldFilterPartOn  # pylint: disable=C0103
