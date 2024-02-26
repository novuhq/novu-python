"""This module is used to gather all DTO definitions related to the Member resource in Novu."""

import dataclasses
from typing import List, Optional

from novu.dto.base import CamelCaseDto, DtoDescriptor
from novu.enums import MemberRole, MemberStatus


@dataclasses.dataclass
class MemberUserDto(CamelCaseDto["MemberUserDto"]):
    """Member user definition"""

    first_name: str
    """Member first name"""

    last_name: str
    """Member last name"""

    email: str
    """Member email"""

    _id: Optional[str] = None
    """User ID in Novu internal storage system"""


@dataclasses.dataclass
class MemberInviteDto(CamelCaseDto["MemberInviteDto"]):
    """Member invite definition"""

    email: str
    """Invited email"""

    token: str
    """Invite token"""

    invitation_date: str
    """Date-time of the invitation"""

    answer_date: Optional[str] = None
    """Date-time of the answer to the invitation"""

    _invite_id: Optional[str] = None
    """Invitation ID in Novu internal storage system"""


@dataclasses.dataclass
class MemberDto(CamelCaseDto["MemberDto"]):
    """Member definition"""

    _id: Optional[str] = None
    """Member ID in Novu internal storage system"""

    _user_id: Optional[str] = None
    """User ID in Novu internal storage system"""

    _organization_id: Optional[str] = None
    """Organization ID in Novu internal storage system"""

    user: Optional[DtoDescriptor[MemberUserDto]] = DtoDescriptor[MemberUserDto](item_cls=MemberUserDto)
    roles: Optional[List[MemberRole]] = None
    invite: Optional[DtoDescriptor[MemberInviteDto]] = DtoDescriptor[MemberInviteDto](item_cls=MemberInviteDto)
    member_status: Optional[MemberStatus] = None
