"""This module is used to gather enumerations related to the Execution resource in Novu"""
from enum import Enum


class ExecutionSource(Enum):
    """This enumeration define all sources possible for an execution in Novu"""

    CREDENTIALS = "Credentials"
    INTERNAL = "Internal"
    PAYLOAD = "Payload"
    WEBHOOK = "Webhook"


class ExecutionStatus(Enum):
    """This enumeration define all status possible for an execution in Novu"""

    SUCCESS = "Success"
    WARNING = "Warning"
    FAILED = "Failed"
    PENDING = "Pending"
    QUEUED = "Queued"
    READ_CONFIRMATION = "ReadConfirmation"
