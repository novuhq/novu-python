"""This module is used to gather helpers reused through the package."""
from typing import Dict


class Singleton(type):
    """Metaclass to use if you need a singleton on your class

    Example:
        >>> from novu.helpers import Singleton
        ...
        >>> class MySingleton(metaclass=Singleton)
        ...    pass
    """

    _instances: Dict[type, type] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]
