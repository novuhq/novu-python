"""This module is used to gather all DTO definitions related to the Notifications resource in Novu"""
import dataclasses
from typing import List, Optional

from novu.dto.base import CamelCaseDto, DtoDescriptor, DtoIterableDescriptor


@dataclasses.dataclass
class ActivityNotificationSubscriberResponseDTO(CamelCaseDto["ActivityNotificationSubscriberResponseDTO"]):
    """Definition of the specific response for an activity notification subscriber request."""

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
class ActivityNotificationTriggerResponseDto(CamelCaseDto["ActivityNotificationTriggerResponseDto"]):
    """Definition of  the triggers for the notifications"""

    type: str
    """The type of trigger"""

    identifier: str
    """The identifier of the trigger"""

    variables: List[dict]
    """The variables for the trigger"""

    subscriber_variables: Optional[List[dict]] = None
    """The subscriber variables for the trigger"""


@dataclasses.dataclass
class ActivityNotificationTemplateResponseDto(CamelCaseDto["ActivityNotificationTemplateResponseDto"]):
    """Definition of  the template used to send the notification"""

    name: str
    """The name of the template"""

    triggers: DtoIterableDescriptor[ActivityNotificationTriggerResponseDto] = DtoIterableDescriptor[
        ActivityNotificationTriggerResponseDto
    ](default_factory=list, item_cls=ActivityNotificationTriggerResponseDto)
    """The triggers for the template"""

    _id: Optional[str] = None
    """The unique ID of the template"""


@dataclasses.dataclass
class ActivityNotificationExecutionDetailResponseDto(CamelCaseDto["ActivityNotificationExecutionDetailResponseDto"]):
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
class ActivityNotificationStepResponseDto(CamelCaseDto["ActivityNotificationStepResponseDto"]):
    """Definition for the Notification for the Step Dto"""

    _id: str
    """The unique ID of the step"""

    active: bool
    """Whether the step is active"""

    filters: dict
    """The filters for the step"""

    template: Optional[dict] = None
    """The template for the step"""


@dataclasses.dataclass
class ActivityNotificationJobResponseDto(CamelCaseDto["ActivityNotificationJobResponseDto"]):
    """Definition of  the job that executed the notification"""

    _id: str
    """The unique ID of the job"""

    step: ActivityNotificationStepResponseDto
    """The step of the job"""

    provider_id: dict
    """The ID of the provider that executed the job"""

    status: str
    """The status of the job"""

    type: DtoDescriptor[ActivityNotificationTriggerResponseDto] = DtoDescriptor[ActivityNotificationTriggerResponseDto](
        item_cls=ActivityNotificationTriggerResponseDto
    )
    execution_details: DtoIterableDescriptor[ActivityNotificationExecutionDetailResponseDto] = DtoIterableDescriptor[
        ActivityNotificationExecutionDetailResponseDto
    ](default_factory=list, item_cls=ActivityNotificationExecutionDetailResponseDto)
    """The execution details of the job"""

    digest: Optional[dict] = None
    """The digest of the job"""

    payload: Optional[dict] = None
    """The payload of the job"""


@dataclasses.dataclass
class ActivityNotificationDto(CamelCaseDto["ActivityNotificationDto"]):
    """Definition of  the notification"""

    _environment_id: str
    """The environment ID of the notification"""

    _organization_id: str
    """The organization ID of the notification"""

    transaction_id: str
    """The transaction ID of the notification"""

    created_at: Optional[str] = None
    """The creation date of the notification"""

    channels: Optional[str] = None
    """The channels of the notification"""

    subscriber: Optional[DtoDescriptor[ActivityNotificationSubscriberResponseDTO]] = DtoDescriptor[
        ActivityNotificationSubscriberResponseDTO
    ](item_cls=ActivityNotificationSubscriberResponseDTO)
    """The subscriber of the notification"""

    template: Optional[ActivityNotificationTemplateResponseDto] = None
    """The template of the notification"""

    jobs: Optional[List[ActivityNotificationJobResponseDto]] = None
    """The jobs of the notification"""

    _id: Optional[str] = None
    """The unique ID of the notification"""
