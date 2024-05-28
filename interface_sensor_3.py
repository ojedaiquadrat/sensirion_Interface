import asyncio
from ble_cli_creator import connect_and_read_data
import sensirion
from sensor_data_handler import getEnvVariables, read_sensor_data



async def main():
  async for s_data in connect_and_read_data(sensirion.sensor_mac_address_3):
         
    print(s_data)
    # Add logic for program termination (e.g., using keyboard interrupt)
  else:
    print("Sensor not connected. Please plug in your sensor and try again!")
    
  await asyncio.sleep(sensirion.DELAY_TIME)
   

asyncio.run(main())
