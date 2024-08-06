#!/usr/bin/env python3
"""
An asynchronous coroutine that takes in an integer argument
that waits for  a random delay between 0 and max_delay
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    pritns random int
    Args:
        max_delay(int): this is the argument
    """
    ran = random.uniform(0, max_delay)
    await asyncio.sleep(ran)
    return ran
