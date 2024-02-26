"""This module is used to gather enumerations related to the Execution resource in Novu"""

from novu.enums.polyfill import StrEnum


class ExecutionSource(StrEnum):
    """This enumeration define all sources possible for an execution in Novu"""

    CREDENTIALS = "Credentials"
    """Execution detail source is credentials"""

    INTERNAL = "Internal"
    """Execution detail source is internal"""

    PAYLOAD = "Payload"
    """Execution detail source is payload"""

    WEBHOOK = "Webhook"
    """Execution detail source is webhook"""


class ExecutionStatus(StrEnum):
    """This enumeration define all status possible for an execution in Novu"""

    SUCCESS = "Success"
    """Execution is successful"""

    WARNING = "Warning"
    """Execution end with a warning"""

    FAILED = "Failed"
    """Execution failed"""

    PENDING = "Pending"
    """Execution is pending"""

    QUEUED = "Queued"
    """Execution is queued"""

    READ_CONFIRMATION = "ReadConfirmation"
    """Execution reading has been confirmed"""
