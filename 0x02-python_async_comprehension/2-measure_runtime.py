#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""
import asyncio
import time
from importlib import import_module as how
async_comprehension = how('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measueres runtime for an asynchronous function
    Return:
        flaot: the return value
    """
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return (end_time - start_time)
