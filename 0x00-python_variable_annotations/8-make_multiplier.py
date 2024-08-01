#!/usr/bin/env python3
"""
Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Function that multiplies
    """
    def fun(n: float):
        """
        Multiplies two floats
        """
        return n * multiplier
    return fun
