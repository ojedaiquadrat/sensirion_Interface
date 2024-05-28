from bleak import BleakClient
from sensor_data_handler import read_sensor_data
import asyncio
import sensirion
import time
#asynchronous generator
async def connect_and_read_data(sensor_mac_address):
  sensirion.connected
  for attempt in range(sensirion.MAX_RETRIES + 1):
    try:
      async with BleakClient(sensor_mac_address) as bleSensorClient:
        print(f"Connection attempt {attempt}: {bleSensorClient.is_connected}")
        sensirion.connected = True
        print("The sensor is connected!")
        #set to get only the latest sample
        await bleSensorClient.write_gatt_char(sensirion.SERVICE_UUID_REQUESTED_SAMPLES, b"\x01\x00", response=False)
        
        while bleSensorClient.is_connected:  # Loop until connection is lost
          start_time = time.time()
          sensirion.scrapped_data = await read_sensor_data(bleSensorClient)
          #print("ble", sensirion.scrapped_data)
          yield sensirion.scrapped_data
          await asyncio.sleep(sensirion.DELAY_TIME)  # Adjustable delay
          end_time = time.time()
          scrapping_frequency = end_time - start_time
          #check the frequency
          #print("Scrapping frenquency: ", scrapping_frequency)
       
          

    except Exception as e:
      print(f"Error connecting to sensor (attempt {attempt+1}): {e}")
      await asyncio.sleep(2)  # Wait before retrying

  if attempt == sensirion.MAX_RETRIES:
    print(f"Failed to connect to sensor after {sensirion.MAX_RETRIES + 1} retries.")
    sensirion.connected = True
    
