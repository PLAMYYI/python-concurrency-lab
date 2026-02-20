import asyncio

async def async_square(n):
    if not isinstance(n, (int, float)):
        raise TypeError("Input must be a number")

    await asyncio.sleep(0.01)
    return n * n


async def run_async_tasks(numbers):
    tasks = [async_square(n) for n in numbers]
    results = await asyncio.gather(*tasks)
    return results