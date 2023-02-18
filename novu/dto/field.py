"""This module is used to gather all DTO definitions related to the Event resource in Novu"""
import dataclasses
from typing import Optional

from novu.dto.base import CamelCaseDto
from novu.enums.field import (
    FieldFilterPartOn,
    FieldFilterPartOperator,
    FieldFilterPartTimeOperator,
)


@dataclasses.dataclass
class FieldFilterPartDto(CamelCaseDto["FieldFilterPartDto"]):
    """Definition of a field filter part"""

    field: str
    """Field of the field filter part"""

    value: str
    """Value of the field filter part

    If the :attr:`on` is set to ``FieldFilterPartOn.IS_ONLINE_IN_LAST``, this value is a number.

    If the :attr:`on` is set to ``FieldFilterPartOn.IS_ONLINE``, this value is a boolean.
    """

    operator: FieldFilterPartOperator
    """Operator of the field filter part"""

    on: FieldFilterPartOn  # pylint: disable=C0103
    """On value of the field filter part"""

    webhook_url: Optional[str] = None
    """Webhook URL, only set if the :attr:`on` is set to ``FieldFilterPartOn.WEBHOOK``"""

    time_operator: Optional[FieldFilterPartTimeOperator] = None
    """Time operator, only set if the :attr:`on` is set to ``FieldFilterPartOn.IS_ONLINE_IN_LAST``"""
