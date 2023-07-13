"""This module is used to gather all DTO definitions related to the Notifications resource in Novu"""
import dataclasses
from typing import List

from novu.dto.base import CamelCaseDto


@dataclasses.dataclass
class SubscriberDto(CamelCaseDto["SubscriberDto"]):
    """Definition of  the subscriber"""

    first_name: str
    """The subscriber's first name"""

    _id: str
    """The subscriber's unique ID"""

    last_name: str
    """The subscriber's last name"""

    email: str
    """The subscriber's email"""

    phone: str
    """The subscriber's phone number"""


@dataclasses.dataclass
class TriggerDto(CamelCaseDto["TriggerDto"]):
    """Definition of  the triggers"""

    type: str
    """The type of trigger"""

    identifier: str
    """The identifier of the trigger"""

    variables: List[dict]
    """The variables for the trigger"""

    subscriber_variables: List[dict]
    """The subscriber variables for the trigger"""


@dataclasses.dataclass
class TemplateDto(CamelCaseDto["TemplateDto"]):
    """Definition of  the template used to send the notification"""

    _id: str
    """The unique ID of the template"""

    name: str
    """The name of the template"""

    triggers: List[TriggerDto]
    """The triggers for the template"""


@dataclasses.dataclass
class ExecutionDetailDto(CamelCaseDto["ExecutionDetailDto"]):
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

    raw: str
    """The raw data of the execution"""

    source: str
    """The source of the execution"""


@dataclasses.dataclass
class StepDto(CamelCaseDto["StepDto"]):
    """Definition of  the step the notification is in"""

    _id: str
    """The unique ID of the step"""

    active: bool
    """Whether the step is active"""

    filters: dict
    """The filters for the step"""

    template: dict
    """The template for the step"""


@dataclasses.dataclass
class JobDto(CamelCaseDto["JobDto"]):
    """Definition of  the job that executed the notification"""

    _id: str
    """The unique ID of the job"""

    type: str
    """The type of the job"""

    digest: dict
    """The digest of the job"""

    execution_details: List[ExecutionDetailDto]
    """The execution details of the job"""

    step: StepDto
    """The step of the job"""

    payload: dict
    """The payload of the job"""

    provider_id: dict
    """The ID of the provider that executed the job"""

    status: str
    """The status of the job"""


@dataclasses.dataclass
class NotificationDto(CamelCaseDto["TemplateDto"]):
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

    subscriber: SubscriberDto
    """The subscriber of the notification"""

    template: TemplateDto
    """The template of the notification"""

    jobs: List[JobDto]
    """The jobs of the notification"""
