"""This module is used to define a configuration ``NovuConfig`` reusable through the package."""
from novu.helpers import Singleton

class NovuConfig(metaclass=Singleton):                                           # pylint: disable=R0903
    """Singleton used to configure global settings for the Novu Client"""

    def __init__(self):
        # Initialize default values or load them from a configuration file
        self._url = ""
        self._api_key = ""

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        """Set the URL of the Novu API to reach."""
        self._url = value

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, value):
        """Set the API Key required to authenticate with the Novu API."""
        self._api_key = value

    @classmethod
    def configure(cls, url: str, api_key: str):
        """Class method provided to configure the singleton data.

        Args:
            url (str): The URL of the Novu API to reach.
            api_key (str): The API Key required to authenticate with the Novu API.
        """
        instance = cls()
        instance.url = url
        instance.api_key = api_key
        return instance

    def clear_configuration(self):
        """Clear the configured values, e.g., for logging out or resetting."""
        self._url = ""
        self._api_key = ""
