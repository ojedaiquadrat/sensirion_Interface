from bleak.backends.characteristic import BleakGATTCharacteristic
import sensirion
import asyncio

def notification_handler(characteristic: BleakGATTCharacteristic, data: bytearray):
	"""
	Callback to read the dataframe notification given by Bleak library

	The first notification contains the header with the information how
	the sampling data are structured. The following frames contain the sampling data.

	Only the latest sampling data is obtained for this specific case
	"""
	sensirion.raw_sensor_dataframe
	sensirion.raw_sensor_dataframe.clear()  # Avoid the first notification and read only the sampling data frame
	sensirion.raw_sensor_dataframe.append(list(data))

def getCO2():
    # print(f"\nRaw Sampling Data frame: {raw_sensor_dataframe}") #check the data frame format
    co2_msb = sensirion.raw_sensor_dataframe[0][7]
    co2_lsb = sensirion.raw_sensor_dataframe[0][6]
    co2_hex = f"{co2_msb:02x}{co2_lsb:02x}"
    co2_dec = int(co2_hex, 16)
    # print(f"- Co2 concentration: {co2_dec} ppm\n")
    return co2_dec

def getTemperature():
    co2_msb = sensirion.raw_sensor_dataframe[0][3]
    co2_lsb = sensirion.raw_sensor_dataframe[0][2]
    co2_hex = f"{co2_msb:02x}{co2_lsb:02x}"
    co2_dec_ticks = int(co2_hex, 16)
    temperature = -45 + ((175.0 * co2_dec_ticks) // ((2**16) - 1))
    # print(f"- Temperature: {temperature} °C\n")
    # return round(temperature,0)
    return int(temperature)

def getHumidity():
    co2_msb = sensirion.raw_sensor_dataframe[0][5]
    co2_lsb = sensirion.raw_sensor_dataframe[0][4]
    co2_hex = f"{co2_msb:02x}{co2_lsb:02x}"
    humidity_dec_ticks = int(co2_hex, 16)
    humidity = (100.0 * humidity_dec_ticks) // ((2**16) - 1)
    # print(f"- Humidity: {humidity} %\n")
    # return round(humidity, 0)
    return int(humidity)

def getEnvVariables():
    co2 = getCO2()
    temperature = getTemperature()
    humidity = getHumidity()
    return {"co2": co2, "temp": temperature, "hum": humidity}


async def read_sensor_data(bleSensorClient):
    await bleSensorClient.start_notify(sensirion.SERVICE_UUID_DATA_TRANSFER, notification_handler)
    await asyncio.sleep(sensirion.SCAN_SENSOR_PERIOD)  # Simulate data reading (replace with actual code)
    await bleSensorClient.stop_notify(sensirion.SERVICE_UUID_DATA_TRANSFER)
    environmental_Variables = getEnvVariables()
    print(environmental_Variables)
    