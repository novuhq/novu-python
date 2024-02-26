"""This module is used to gather enumerations related to the Provider resource in Novu"""

from typing import Union

from novu.enums.polyfill import StrEnum


class CredentialsKeyEnum(StrEnum):
    """This enumeration define possible key in a Novu credentials dict"""

    API_KEY = "apiKey"
    """Api key"""

    USER = "user"
    """User"""

    SECRET_KEY = "secretKey"  # nosec: B105
    """Secret key"""

    DOMAIN = "domain"
    """Domain"""

    PASSWORD = "password"  # nosec: B105
    """Password"""

    HOST = "host"
    """Host"""

    PORT = "port"
    """Port"""

    SECURE = "secure"
    """Secure"""

    REGION = "region"
    """Region"""

    ACCOUNT_SID = "accountSid"
    """Account SID"""

    MESSAGE_PROFILE_ID = "messageProfileId"
    """Message profile ID"""

    TOKEN = "token"  # nosec: B105
    """Token"""

    FROM = "from"
    """From"""

    SENDER_NAME = "senderName"
    """Sender name"""

    APPLICATION_ID = "applicationId"
    """Application ID"""

    CLIENT_ID = "clientId"
    """Client ID"""

    PROJECT_NAME = "projectName"
    """Project name"""

    SERVICE_ACCOUNT = "serviceAccount"
    """Service account"""

    BASE_URL = "baseUrl"
    """Base URL"""

    WEBHOOK_URL = "webhookUrl"
    """Webhook URL"""


class EmailProviderIdEnum(StrEnum):
    """This enumeration define possible email provider ID.

    For more details about their configuration, see https://docs.novu.co/channels/email/
    """

    EMAILJS = "emailjs"
    """EmailJS mail provider, see """

    MAILGUN = "mailgun"
    """MailGun mail provider"""

    MAILJET = "mailjet"
    """MailJet mail provider"""

    MANDRILL = "mandrill"
    """Mandrill mail provider"""

    CUSTOM_SMTP = "nodemailer"
    """Custom SMTP provider, for example a nodemailer"""

    POSTMARK = "postmark"
    """Postmark mail provider"""

    SENDGRID = "sendgrid"
    """SendGrid mail provider"""

    SENDINBLUE = "sendinblue"
    """SendInBlue mail provider"""

    SES = "ses"
    """Amazon SES mail provider"""

    NETCORE = "netcore"
    """NetCore mail provider"""

    INFOBIP = "infobip-email"
    """InfoBIP mail provider"""

    MAILERSEND = "mailersend"
    """Mailer Send provider"""

    CLICKATELL = "clickatell"
    """Click-a-tell mail provider"""

    OUTLOOK365 = "outlook365"
    """Outlook 365 mail provider"""

    NOVU = "novu-email"
    """Novu internal mail provider"""


class SmsProviderIdEnum(StrEnum):
    """This enumeration define possible sms provider ID"""

    NEXMO = "nexmo"
    """Nexmo sms provider"""

    PLIVO = "plivo"
    """Plivo sms provider"""

    SMS77 = "sms77"
    """SMS 77 provider"""

    SNS = "sns"
    """Amazon SNS provider"""

    TELNYX = "telnyx"
    """Telnyx sms provider"""

    TWILIO = "twilio"
    """Twilio sms provider"""

    GUPSHUP = "gupshup"
    """Gupshup sms provider"""

    FIRETEXT = "firetext"
    """Firetext sms provider"""

    INFOBIP = "infobip-sms"
    """InfoBIP sms provider"""

    BURST_SMS = "burst-sms"
    """BurstSMS provider"""

    CLICKATELL = "clickatell"
    """Click-a-tell sms provider"""


class ChatProviderIdEnum(StrEnum):
    """This enumeration define possible chat provider ID"""

    SLACK = "slack"
    """Slack provider for chat messages"""

    DISCORD = "discord"
    """Discord provider for chat messages"""

    MS_TEAMS = "msteams"
    """MS Teams provider for chat messages"""


class PushProviderIdEnum(StrEnum):
    """This enumeration define possible push provider ID"""

    FCM = "fcm"
    """FCM notification push provider"""

    APNS = "apns"
    """APNS notification push provider"""

    EXPO = "expo"
    """EXPO notification push provider"""


class InAppProviderIdEnum(StrEnum):
    """This enumeration define possible in_app provider ID"""

    NOVU = "novu"
    """The only in-app provider, Novu"""


ProviderIdEnum = Union[
    SmsProviderIdEnum, PushProviderIdEnum, ChatProviderIdEnum, EmailProviderIdEnum, InAppProviderIdEnum
]
"""Type to define the notion of provider ID, which is one of sms, push, chat, email, or in_app provider ID."""
