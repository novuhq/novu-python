"""This module is used to define a configuration ``NovuConfig`` reusable through the package."""
from novu.helpers import Singleton


class NovuConfig(metaclass=Singleton):  # pylint: disable=R0903
    """Singleton used to configure globally URL and API_KEY for the Novu Client"""

    url: str
    """The URL of the Novu API to reach"""

    api_key: str
    """The API Key required to auth on the Novu API"""

    @classmethod
    def configure(cls, url: str, api_key: str):
        """Class method provided to initialise the singleton data.

        Args:
            url: The URL of the Novu API to reach.
            api_key: The API Key required to auth on the Novu API.
        """
        cls().url = url
        cls().api_key = api_key
