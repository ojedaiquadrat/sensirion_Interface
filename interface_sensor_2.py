import asyncio
from ble_cli_creator import connect_and_read_data
import sensirion
from sensor_data_handler import getEnvVariables, read_sensor_data



async def main():
  async for sensirion_data in connect_and_read_data(sensirion.sensor_mac_address_2):
    #sensirion_data is the variable to get the data     
    print(sensirion_data)
    
  else:
    # Add logic for program termination (e.g., using keyboard interrupt)
    print("Sensor not connected. Please plug in your sensor and try again")
    
  await asyncio.sleep(sensirion.DELAY_TIME)
   

asyncio.run(main())
