"""Polyfill of backports related to enums."""
try:
    from enum import StrEnum  # type: ignore[attr-defined]
except ImportError:
    from enum import Enum

    class StrEnum(str, Enum):  # type: ignore[no-redef]
        """Redefinition of ``StrEnum`` to backport this class from python 3.10."""


__all__ = ["StrEnum"]
