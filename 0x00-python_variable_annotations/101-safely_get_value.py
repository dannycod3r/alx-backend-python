#!/usr/bin/env python3
"""Modify function with type annotation"""
from typing import Any, Mapping, TypeVar, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None]=None) -> Union[Any, T]:
    """return dictionary or default"""
    if key in dct:
        return dct[key]
    else:
        return default
