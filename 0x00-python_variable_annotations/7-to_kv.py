#!/usr/bin/env python3
"""Module supplies funtion that
   return a tuple"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return tuple"""
    return (k, float(v ** 2))
