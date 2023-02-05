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
