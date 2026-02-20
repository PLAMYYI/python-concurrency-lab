import asyncio

async def fetch_data(name, delay):
    print(f"Start fetching {name}")
    await asyncio.sleep(delay)
    print(f"Finished fetching {name}")
    return name

async def main():
    tasks = [
        fetch_data("API1", 2),
        fetch_data("API2", 3),
        fetch_data("API3", 1),
    ]

    results = await asyncio.gather(*tasks)
    print("All tasks done:", results)

if __name__ == "__main__":
    asyncio.run(main())