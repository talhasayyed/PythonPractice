import asyncio
import random

async def fetch_data(name):
    print(f"Start fetching {name}")
    # await asyncio.sleep(2)  # Simulate I/O wait
    random_seconds = random.randint(1,5) # 1-5 seconds
    await asyncio.sleep(random_seconds)  # Simulate I/O wait
    print(f"Done fetching {name}")
    return f"Data from {name}"

async def main():
    results = await asyncio.gather(
        fetch_data("API-1"),
        fetch_data("API-2"),
        fetch_data("API-3"),
    )
    print(results)
    print(type(results))

asyncio.run(main())

""" Output
Start fetching API-1
Start fetching API-2
Start fetching API-3
Done fetching API-1
Done fetching API-3
Done fetching API-2
['Data from API-1', 'Data from API-2', 'Data from API-3']
<class 'list'>
"""
