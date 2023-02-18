"""This module is used to gather all DTO definitions related to the Event resource in Novu"""
import dataclasses

from novu.dto.base import CamelCaseDto
from novu.enums.field import FieldFilterPartOn, FieldFilterPartOperator


@dataclasses.dataclass
class FieldFilterPartDto(CamelCaseDto["FieldFilterPartDto"]):
    """Definition of a field filter part"""

    field: str
    """Field of the field filter part"""

    value: str
    """Value of the field filter part"""

    operator: FieldFilterPartOperator
    """Operator of the field filter part"""

    on: FieldFilterPartOn  # pylint: disable=C0103
    """On value of the field filter part"""
