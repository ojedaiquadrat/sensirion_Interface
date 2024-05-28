import asyncio
from ble_cli_creator import connect_and_read_data
import sensirion
from sensor_data_handler import getEnvVariables, read_sensor_data

# Define reading frequency
reading_frequency = 1

async def main():
  async for s_data in connect_and_read_data():
         
    print(s_data)
    # Add logic for program termination (e.g., using keyboard interrupt)
  else:
    print("Sensor not connected. Please plug in your sensor and try again")
    
  await asyncio.sleep(reading_frequency)
   

asyncio.run(main())
