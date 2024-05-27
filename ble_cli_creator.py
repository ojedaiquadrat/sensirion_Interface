from bleak import BleakClient
from sensor_data_handler import read_sensor_data
import asyncio
import sensirion

async def connect_and_read_data():
  sensirion.connected
  for attempt in range(sensirion.MAX_RETRIES + 1):
    try:
      async with BleakClient(sensirion.sensor_mac_address) as bleSensorClient:
        print(f"Connection attempt {attempt}: {bleSensorClient.is_connected}")
        sensirion.connected = True
        print("The sensor is connected!")
        #set to get only the latest sample
        await bleSensorClient.write_gatt_char(sensirion.SERVICE_UUID_REQUESTED_SAMPLES, b"\x01\x00", response=False)
        
        while bleSensorClient.is_connected:  # Loop until connection is lost
          await read_sensor_data(bleSensorClient)
          await asyncio.sleep(3)  # Adjustable delay

    except Exception as e:
      print(f"Error connecting to sensor (attempt {attempt+1}): {e}")
      await asyncio.sleep(2)  # Wait before retrying

  if attempt == sensirion.MAX_RETRIES:
    print(f"Failed to connect to sensor after {sensirion.MAX_RETRIES} retries.")
    connected = False