"""
Novu SDK
========

Provides
  1. Wrapper to interact with Novu API for each resource
  2. DTO dataclasses to parse Novu resources.
  3. Enumerations from Novu.

Available subpackages
---------------------

api
    Wrapper to interact with Novu API for each resource
dto
    DTO dataclasses to parse Novu resources.
enums
    Enumerations from Novu.
"""

from novu import api, dto, enums
from novu.config import NovuConfig

__all__ = ["api", "dto", "enums", "NovuConfig"]
