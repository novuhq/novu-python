"""This module is used to gather enumerations related to the Step Filter resource in Novu"""
from enum import Enum


class StepFilterType(Enum):
    """This enumeration define possible type for a step filter"""

    BOOL = "BOOLEAN"
    """Boolean filter"""

    TEXT = "TEXT"
    """Text filter"""

    DATE = "DATE"
    """Date filter"""

    NUMBER = "NUMBER"
    """Number filter"""

    STATEMENT = "STATEMENT"
    """Statement filter"""

    LIST = "LIST"
    """List filter"""

    MULTI_LIST = "MULTI_LIST"
    """Multi-list filter"""

    GROUP = "GROUP"
    """Group filter"""


class StepFilterValue(Enum):
    """This enumeration define possible value for a step filter"""

    AND = "AND"
    """And operator"""

    OR = "OR"
    """Or operator"""
