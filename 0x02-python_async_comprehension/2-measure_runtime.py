#!/usr/bin/env python3
"""
Measure the time taken for an async function
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    return total runtime of async comprehension
    """
    start = time.time()

    await asyncio.gather(async_comprehension())

    end = time.time()
    runtime = end - start
    return runtime
