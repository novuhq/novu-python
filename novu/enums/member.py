"""This module is used to gather enumerations related to the Provider resource in Novu"""
from novu.enums.polyfill import StrEnum


class MemberRole(StrEnum):
    """This enumeration define possible role for a member"""

    ADMIN = "admin"
    """The member is an administrator"""

    MEMBER = "member"
    """The member is a simple member"""


class MemberStatus(StrEnum):
    """This enumeration define possible status for a member"""

    NEW = "new"
    """The member is new"""

    ACTIVE = "active"
    """The member is active"""

    INVITED = "invited"
    """The member has been invited"""
