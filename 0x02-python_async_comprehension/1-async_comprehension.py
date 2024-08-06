#!/usr/bin/env python3
"""
Async comprehension
"""
import asyncio
from typing import AsyncGenerator
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> AsyncGenerator[float, None]:
    """
    Async comprehension function
    Return: async comprehension
    """
    res = [i async for i in async_generator for _ in range(10)]
    return res
