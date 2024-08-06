#!/usr/bin/env python3
"""
A coroutine called async_generator that takes no arguments.
"""
import asyncio
import random


async def async_generator():
    """
    async generator function
    Return: returns random value asynchronously
    """

    for i in range(10):
        ran = random.uniform(0, 10)
        yield ran
        await asyncio.sleep(1)
