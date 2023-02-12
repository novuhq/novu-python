"""This module is used to gather enumerations related to the Field resource in Novu"""
from enum import Enum


class FieldFilterPartOperator(Enum):
    """This enumeration define possible operator for a field filter part"""

    LARGER = "LARGER"
    SMALLER = "SMALLER"
    LARGER_EQUAL = "LARGER_EQUAL"
    SMALLER_EQUAL = "SMALLER_EQUAL"
    EQUAL = "EQUAL"
    NOT_EQUAL = "NOT_EQUAL"
    ALL_IN = "ALL_IN"
    ANY_IN = "ANY_IN"
    NOT_IN = "NOT_IN"
    BETWEEN = "BETWEEN"
    NOT_BETWEEN = "NOT_BETWEEN"
    LIKE = "LIKE"
    NOT_LIKE = "NOT_LIKE"
    IN = "IN"


class FieldFilterPartOn(Enum):
    """This enumeration define possible trigger (``on``) for a field filter part"""

    SUBSCRIBER = "subscriber"
    PAYLOAD = "payload"
