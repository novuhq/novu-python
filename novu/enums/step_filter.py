"""This module is used to gather enumerations related to the Step Filter resource in Novu"""
from enum import Enum


class StepFilterType(Enum):
    """This enumeration define possible type for a step filter"""

    BOOL = "BOOLEAN"
    TEXT = "TEXT"
    DATE = "DATE"
    NUMBER = "NUMBER"
    STATEMENT = "STATEMENT"
    LIST = "LIST"
    MULTI_LIST = "MULTI_LIST"
    GROUP = "GROUP"


class StepFilterValue(Enum):
    """This enumeration define possible value for a step filter"""

    AND = "AND"
    OR = "OR"
