import asyncio
from ble_cli_creator import connect_and_read_data
import sensirion

# Define reading frequency
reading_frequency = 1

async def main():
  while True:
    if not sensirion.connected:
      await connect_and_read_data()
    # Add logic for program termination (e.g., using keyboard interrupt)
    else:
      print("Sensor not connected. Please plug in your sensor and try again")
      break
    await asyncio.sleep(reading_frequency)
   

asyncio.run(main())
