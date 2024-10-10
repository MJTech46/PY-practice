"""async means the function can perform tasks without stopping the rest of the program from running. """
import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulates a network request with a 2-second delay
    return "Data fetched"

async def main():
    print("Starting...")
    result = await fetch_data()  # Await the asynchronous function
    print(result)
    print("Finished")

# Running the async function
asyncio.run(main())
