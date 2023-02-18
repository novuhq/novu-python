"""This module is used to gather enumerations related to the Channel resource in Novu"""
from enum import Enum


class Channel(Enum):
    """This enumeration define all available channel in Novu"""

    EMAIL = "email"
    """Email channel (Custom SMTP, EmailJS, MailerSend, Mailjet, Outlook 365,
    Postmark, SendGrid, Sendinblue, Amazon SES, ...)"""

    SMS = "sms"
    """SMS channel (SMS77, AWS SNS, Telnyx, Twilio SMS, ...)"""

    IN_APP = "in_app"
    """In APP channel"""

    CHAT = "chat"
    """Chat channel (discord, MS Teams, Slack, ...)"""

    PUSH = "push"
    """Push channel (Expo, Firebase Cloud Messaging, ...)"""


class ChannelExtended(Enum):
    """
    This enumeration define all available channel in Novu and intermediate provider between channel.

    This definition is useful to determine if a block is a channel or a digest for example.
    """

    EMAIL = "email"
    """Email channel (Custom SMTP, EmailJS, MailerSend, Mailjet, Outlook 365,
    Postmark, SendGrid, Sendinblue, Amazon SES, ...)"""

    SMS = "sms"
    """SMS channel (SMS77, AWS SNS, Telnyx, Twilio SMS, ...)"""

    IN_APP = "in_app"
    """In APP channel"""

    CHAT = "chat"
    """Chat channel (discord, MS Teams, Slack, ...)"""

    PUSH = "push"
    """Push channel (Expo, Firebase Cloud Messaging, ...)"""

    DIGEST = "digest"
    """Used to aggregate message on certain conditions"""

    TRIGGER = "trigger"
    """Trigger to start the notification template"""

    DELAY = "delay"
    """A delay in the notification template"""
