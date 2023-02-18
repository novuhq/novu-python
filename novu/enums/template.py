"""This module is used to gather enumerations related to the Template resource in Novu"""
from enum import Enum


class TemplateVariableTypeEnum(Enum):
    """This enumeration define possible type for a variable in a template"""

    STRING = "String"
    """String variable"""

    LIST = "Array"
    """List variable"""

    BOOL = "Boolean"
    """Boolean variable"""
