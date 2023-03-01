"""This module is used to gather helpers reused through the package."""
import importlib
from typing import Dict


class Singleton(type):
    """Metaclass to use if you need a singleton on your class

    Example:
        >>> from novu.helpers import Singleton
        >>> class MySingleton(metaclass=Singleton)
        ...    pass
    """

    _instances: Dict[type, type] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class SentryProxy(metaclass=Singleton):
    """Simple singleton to proxy all methods of Sentry SDK

    This class allows, in the application, to make sentry optional, in terms of installation, without effort.
    """

    def __init__(self) -> None:
        self.import_module()

    def import_module(self):
        """Method to try to load the sentry_sdk module or set it to None"""
        try:
            self.sentry_sdk = importlib.import_module("sentry_sdk")
        except ModuleNotFoundError:
            self.sentry_sdk = None

    def __getattr__(self, attr):
        if self.sentry_sdk:
            return getattr(self.sentry_sdk, attr, None)
        return lambda *args, **kwargs: None
