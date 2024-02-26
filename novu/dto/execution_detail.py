"""This module is used to gather all DTO definitions related to the Execution Detail resource in Novu"""

import dataclasses
from typing import Optional

from novu.dto.base import CamelCaseDto
from novu.enums import ChannelExtended, ExecutionSource, ExecutionStatus


@dataclasses.dataclass
class ExecutionDetailDto(CamelCaseDto["ExecutionDetailDto"]):  # pylint: disable=R0902
    """Definition of an execution detail"""

    _id: Optional[str] = None
    """Execution detail ID in Novu internal storage system"""

    _job_id: Optional[str] = None
    """Job ID in Novu internal storage system"""

    _environment_id: Optional[str] = None
    """Environment ID in Novu internal storage system"""

    _organization_id: Optional[str] = None
    """Organization ID in Novu internal storage system"""

    _notification_id: Optional[str] = None
    """Notification ID in Novu internal storage system"""

    _notification_template_id: Optional[str] = None
    """Notification template ID in Novu internal storage system"""

    _subscriber_id: Optional[str] = None
    """Subscriber ID in Novu internal storage system"""

    _message_id: Optional[str] = None
    """Message ID in Novu internal storage system"""

    provider_id: Optional[str] = None
    """Provider ID in Novu internal storage system"""

    transaction_id: Optional[str] = None
    """Transaction ID in Novu internal storage system"""

    channel: Optional[ChannelExtended] = None
    """Channel used to the execution (or logical step like digest or trigger)"""

    detail: Optional[str] = None
    """Details of the execution"""

    source: Optional[ExecutionSource] = None
    """Source of the execution"""

    status: Optional[ExecutionStatus] = None
    """Status of the execution"""

    is_test: Optional[bool] = None
    """If this execution is related to a test"""

    is_retry: Optional[bool] = None
    """If this execution detail is related to a retry"""

    raw: Optional[str] = None
    """Raw details of the execution"""

    created_at: Optional[str] = None
    """Creation date of the execution detail"""

    updated_at: Optional[str] = None
    """Last update date of the execution detail"""
