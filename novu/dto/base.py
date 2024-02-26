"""This module is used to defined all helpers to parse and send well-formatted data to the Novu API"""

import dataclasses
import re
from typing import ClassVar, Generic, Iterable, List, Optional, Type, TypeVar, Union

CAMELIZE_PATTERN = re.compile(r"(?:^|_)(.)")
UNDERSCORE_PATTERN_1 = re.compile(r"([A-Z]+)([A-Z][a-z])")
UNDERSCORE_PATTERN_2 = re.compile(r"([a-z\d])([A-Z])")


def snake_case_to_camel_case(string: str, upper_camel_case: bool = False) -> str:
    """Convert strings to CamelCase.

    Examples:
        >>> snake_case_to_camel_case("device_type")
        'DeviceType'
        >>> snake_case_to_camel_case("device_type", False)
        'deviceType'

    Args:
        string: The string to camelize
        upper_camel_case:
            If set to `True` :func:`snake_case_to_camel_case` converts strings to UpperCamelCase.
            If set to `False` :func:`snake_case_to_camel_case` produces lowerCamelCase.
            Defaults to `False`.
    """
    if upper_camel_case:
        return re.sub(CAMELIZE_PATTERN, lambda m: m.group(1).upper(), string)

    return string[0].lower() + snake_case_to_camel_case(string, True)[1:]


def camel_case_to_snake_case(word: str) -> str:
    """Make an underscored, lowercase form from the expression in the string.

    Example:
        >>> camel_case_to_snake_case("DeviceType")
        'device_type'
    """
    word = re.sub(UNDERSCORE_PATTERN_1, r"\1_\2", word)
    word = re.sub(UNDERSCORE_PATTERN_2, r"\1_\2", word)
    return word.replace("-", "_").lower()


_T = TypeVar("_T")


@dataclasses.dataclass
class CamelCaseDto(Generic[_T]):
    """A generic dataclass that allows to convert data from Novu API written in
    camel case to python (in snake_case) and back."""

    snake_case_to_camel_case_ignored: ClassVar[List[str]] = []
    """List of fields which we don't want to camelize."""

    camel_case_fields: ClassVar[Optional[List[str]]] = None
    """List of fields to define in the dict during :meth:`to_camel_case`.

    If this list is not defined, we have taken all the fields from the data class."""

    @classmethod
    def from_camel_case(cls: Type[_T], data: dict) -> _T:
        """Helper to parse a camel case dict"""
        fields = {f.name: f.type for f in dataclasses.fields(cls)}  # type: ignore[arg-type]
        kwargs = {}
        for key, val in data.items():
            _key = camel_case_to_snake_case(key)
            if _key in fields.keys():
                kwargs[_key] = fields[_key].from_camel_case(val) if hasattr(fields[_key], "from_camel_case") else val

        return cls(**kwargs)

    def to_camel_case(self) -> dict:
        """Helper to build a camel case dict"""
        if self.camel_case_fields:
            # pylint: disable=E1135
            return {
                snake_case_to_camel_case(k) if k not in self.snake_case_to_camel_case_ignored else k: v
                for k, v in dataclasses.asdict(self).items()
                if k in self.camel_case_fields
            }
        return {
            snake_case_to_camel_case(k) if k not in self.snake_case_to_camel_case_ignored else k: v
            for k, v in dataclasses.asdict(self).items()
        }


_C_co = TypeVar("_C_co", bound=CamelCaseDto, covariant=True)


class DtoDescriptor(Generic[_C_co]):
    """The Dto descriptor is used on :func:`dataclasses.dataclass` to help them parse sub-struct defined using
    the :class:`~novu.dto.base.CamelCaseDto` class during :meth:`~novu.dto.base.CamelCaseDto.from_camel_case` calls
    on Novu API response.

    Example:
        >>> @dataclasses.dataclass
        ... class SubscriberPreferenceDto(CamelCaseDto["SubscriberPreferenceDto"]):
        ...     template: DtoDescriptor[SubscriberPreferenceTemplateDto] = (
        ...         DtoDescriptor[SubscriberPreferenceTemplateDto](item_cls=SubscriberPreferenceTemplateDto)
        ...     )
    """

    def __init__(self, item_cls: Type[CamelCaseDto]):
        self._name: Optional[str] = None
        self._item_cls = item_cls

    def __set_name__(self, _, name: str):
        self._name = f"_{name}"

    def __get__(self, obj, _) -> Optional[_C_co]:
        if obj is None:
            return None

        return getattr(obj, self._name, None) if self._name else None

    def __set__(self, obj, value: Union[_C_co, dict]) -> None:
        if self._name:  # pragma: no branch (ignore because should never append as descriptor, branch is just for mypy)
            setattr(obj, self._name, self._item_cls.from_camel_case(value) if isinstance(value, dict) else value)


class DtoIterableDescriptor(Generic[_C_co]):
    """The Dto iterable descriptor is used on :func:`dataclasses.dataclass` to help them parse iterable sub-struct
    defined using the :class:`~novu.dto.base.CamelCaseDto` class during
    :meth:`~novu.dto.base.CamelCaseDto.from_camel_case` calls on Novu API response.

    Example:
        >>> @dataclasses.dataclass
        ... class PaginatedTopicDto(CamelCaseDto["PaginatedTopicDto"]):
        ...     data: DtoIterableDescriptor[TopicDto] = DtoIterableDescriptor[TopicDto](
        ...         default_factory=list, item_cls=TopicDto
        ...     )
    """

    def __init__(self, default_factory, item_cls: Type[_C_co]):
        self.default_factory = default_factory
        self._name: Optional[str] = None
        self._item_cls = item_cls

    def __set_name__(self, _, name):
        self._name = f"_{name}"

    def __get__(self, obj, _) -> Optional[Iterable[_C_co]]:
        if obj is None:
            return None

        return getattr(obj, self._name, None) if self._name else None

    def __set__(self, obj, value: Union[Iterable[_C_co], Iterable[dict]]) -> None:
        if self._name and value is not None:
            setattr(obj, self._name, [self._item_cls.from_camel_case(v) if isinstance(v, dict) else v for v in value])
