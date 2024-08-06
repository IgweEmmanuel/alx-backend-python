#!/usr/bin/env python3
"""
A coroutine called async_generator that takes no arguments.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    async generator function
    Return: returns random value asynchronously
    """

    for _ in range(10):
        ran = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield ran
