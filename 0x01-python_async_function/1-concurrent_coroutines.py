#!/usr/bin/env python3
"""
Executing multiple coroutine at the same time
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Retruns multiple coroutines in delayed time
    Args:
        n(int): parameter 1 with int type
        max_delay(int): second parameter.
    """
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    # Collect the delays in the order they complete
    return delays
