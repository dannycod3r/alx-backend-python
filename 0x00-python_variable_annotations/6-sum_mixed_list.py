#!/usr/bin/env python3
"""Module supplies fucntion that
   returns sum of list of int and floats"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of the mixed list"""
    return sum(mxd_lst)
