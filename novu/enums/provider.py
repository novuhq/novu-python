"""This module is used to gather enumerations related to the Provider resource in Novu"""
from enum import Enum
from typing import Union


class CredentialsKeyEnum(Enum):
    """This enumeration define possible key in a Novu credentials dict"""

    API_KEY = "apiKey"
    USER = "user"
    SECRET_KEY = "secretKey"  # nosec: B105
    DOMAIN = "domain"
    PASSWORD = "password"  # nosec: B105
    HOST = "host"
    PORT = "port"
    SECURE = "secure"
    REGION = "region"
    ACCOUNT_SID = "accountSid"
    MESSAGE_PROFILE_ID = "messageProfileId"
    TOKEN = "token"  # nosec: B105
    FROM = "from"
    SENDER_NAME = "senderName"
    APPLICATION_ID = "applicationId"
    CLIENT_ID = "clientId"
    PROJECT_NAME = "projectName"
    SERVICE_ACCOUNT = "serviceAccount"
    BASE_URL = "baseUrl"
    WEBHOOK_URL = "webhookUrl"


class EmailProviderIdEnum(Enum):
    """This enumeration define possible email provider ID"""

    EMAILJS = "emailjs"
    MAILGUN = "mailgun"
    MAILJET = "mailjet"
    MANDRILL = "mandrill"
    CUSTOM_SMTP = "nodemailer"
    POSTMARK = "postmark"
    SENDGRID = "sendgrid"
    SENDINBLUE = "sendinblue"
    SES = "ses"
    NETCORE = "netcore"
    INFOBIP = "infobip-email"
    MAILERSEND = "mailersend"
    CLICKATELL = "clickatell"
    OUTLOOK365 = "outlook365"
    NOVU = "novu-email"


class SmsProviderIdEnum(Enum):
    """This enumeration define possible sms provider ID"""

    NEXMO = "nexmo"
    PLIVO = "plivo"
    SMS77 = "sms77"
    SNS = "sns"
    TELNYX = "telnyx"
    TWILIO = "twilio"
    GUPSHUP = "gupshup"
    FIRETEXT = "firetext"
    INFOBIP = "infobip-sms"
    BURST_SMS = "burst-sms"
    CLICKATELL = "clickatell"


class ChatProviderIdEnum(Enum):
    """This enumeration define possible chat provider ID"""

    SLACK = "slack"
    DISCORD = "discord"
    MS_TEAMS = "msteams"


class PushProviderIdEnum(Enum):
    """This enumeration define possible push provider ID"""

    FCM = "fcm"
    APNS = "apns"
    EXPO = "expo"


class InAppProviderIdEnum(Enum):
    """This enumeration define possible in_app provider ID"""

    NOVU = "novu"


ProviderIdEnum = Union[
    SmsProviderIdEnum, PushProviderIdEnum, ChatProviderIdEnum, EmailProviderIdEnum, InAppProviderIdEnum
]
"""Type to define the notion of provider ID, which is one of sms, push, chat, email, or in_app provider ID."""
