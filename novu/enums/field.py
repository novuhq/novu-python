"""This module is used to gather enumerations related to the Field resource in Novu"""
from enum import Enum


class FieldFilterPartOperator(Enum):
    """This enumeration define possible operator for a field filter part"""

    LARGER = "LARGER"
    """Larger operator (``>``)"""

    SMALLER = "SMALLER"
    """Smaller operator (``<``)"""

    LARGER_EQUAL = "LARGER_EQUAL"
    """Larger or equal operator (``>=``)"""

    SMALLER_EQUAL = "SMALLER_EQUAL"
    """Smaller or equal operator (``<=``)"""

    EQUAL = "EQUAL"
    """Equal operator (``==``)"""

    NOT_EQUAL = "NOT_EQUAL"
    """Not equal operator (``!=``)"""

    ALL_IN = "ALL_IN"
    """All in operator, which is like a python :func:`all`"""

    ANY_IN = "ANY_IN"
    """Any in operator, which is like a python :func:`any`"""

    NOT_IN = "NOT_IN"
    """Not equal operator (``not in``)"""

    BETWEEN = "BETWEEN"
    """Between operator (``lower_range <= item <= upper_range``)"""

    NOT_BETWEEN = "NOT_BETWEEN"
    """Not between operator (``not (lower_range <= item <= upper_range)``)"""

    LIKE = "LIKE"
    """LIKE operator (``sentence.find(item)``)"""

    NOT_LIKE = "NOT_LIKE"
    """Not LIKE operator (``not sentence.find(item)``)"""

    IN = "IN"
    """Not equal operator (``in``)"""


class FieldFilterPartOn(Enum):
    """This enumeration define possible trigger (``on``) for a field filter part"""

    SUBSCRIBER = "subscriber"
    """Filter using the subscriber's data"""

    PAYLOAD = "payload"
    """Filter using the payload's data"""

    WEBHOOK = "webhook"
    """Filter using the webhook's data"""

    IS_ONLINE = "isOnline"
    """Allow to check if the subscriber is online"""

    IS_ONLINE_IN_LAST = "isOnlineInLast"
    """Allow to check if the subscriber is online in last X given minutes"""


class FieldFilterPartTimeOperator(Enum):
    """
    This enumeration define possible operator for a filed filter part which is used if
    ``FieldFilterPartDto.on`` is set to ``FieldFilterPartOn.IS_ONLINE_IN_LAST``"""

    MINUTES = "minutes"
    """The minutes operator"""

    HOURS = "hours"
    """The hours operator"""

    DAYS = "days"
    """The days operator"""
