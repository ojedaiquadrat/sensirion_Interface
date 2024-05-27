import asyncio
from ble_cli_creator import connect_and_read_data
import sensirion

# Define reading frequency
reading_frequency = 5

async def main():
  while True:
    if not sensirion.connected:
      await connect_and_read_data()
    # Add logic for program termination (e.g., using keyboard interrupt)
    await asyncio.sleep(reading_frequency)

asyncio.run(main())
