"""This module is used to gather all DTO definitions related to the Notifications resource in Novu"""
import dataclasses
from typing import List, Optional

from novu.dto.base import CamelCaseDto
from novu.dto.notification_template import (
    NotificationBaseStepDto,
    NotificationBaseTemplateDto,
)

# from novu.dto.subscriber import SubscriberBaseDto


@dataclasses.dataclass
class NotificationSubscriberBaseDto(CamelCaseDto["NotificationSubscriberBaseDto"]):
    """Base class for the subscriber in both notification and subscriber"""

    _id: str
    """The subscriber's unique ID"""

    email: Optional[str] = None
    """The subscriber's email"""

    first_name: Optional[str] = None
    """The subscriber's first name"""

    last_name: Optional[str] = None
    """The subscriber's last name"""

    phone: Optional[str] = None
    """The subscriber's phone number"""


@dataclasses.dataclass
class NotificationExecutionDetailDto(CamelCaseDto["NotificationExecutionDetailDto"]):
    """Definition of  the execution of the notification"""

    _id: str
    """The unique ID of the execution"""

    _job_id: str
    """The ID of the job that executed the notification"""

    status: str
    """The status of the execution"""

    detail: str
    """The detail of the execution"""

    is_retry: bool
    """Whether the execution is a retry"""

    is_test: bool
    """Whether the execution is a test"""

    provider_id: dict
    """The ID of the provider that executed the notification"""

    source: str
    """The source of the execution"""

    raw: Optional[str] = None
    """The raw data of the execution"""


@dataclasses.dataclass
class NotificationJobDto(CamelCaseDto["NotificationJobDto"]):
    """Definition of  the job that executed the notification"""

    _id: str
    """The unique ID of the job"""

    type: str
    """The type of the job"""

    execution_details: List[NotificationExecutionDetailDto]
    """The execution details of the job"""

    step: NotificationBaseStepDto
    """The step of the job"""

    provider_id: dict
    """The ID of the provider that executed the job"""

    status: str
    """The status of the job"""

    digest: Optional[dict] = None
    """The digest of the job"""

    payload: Optional[dict] = None
    """The payload of the job"""


@dataclasses.dataclass
class NotificationDto(CamelCaseDto["NotificationDto"]):
    """Definition of  the notification"""

    _id: str
    """The unique ID of the notification"""

    _environment_id: str
    """The environment ID of the notification"""

    _organization_id: str
    """The organization ID of the notification"""

    transaction_id: str
    """The transaction ID of the notification"""

    created_at: str
    """The creation date of the notification"""

    channels: str
    """The channels of the notification"""

    subscriber: NotificationSubscriberBaseDto
    """The subscriber of the notification"""

    template: NotificationBaseTemplateDto
    """The template of the notification"""

    jobs: List[NotificationJobDto]
    """The jobs of the notification"""
