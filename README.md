# Sensirion Gadget Simple Interface

## Description
This project provides Python scripts to acquire environmental data (CO2 concentration, temperature, and humidity) from a [Sensirion Gadget](https://sensirion.com/products/catalog/SCD4x-CO2-Gadget).

Environmental Parameters Acquired:

* CO2 concentration (ppm)
* Temperature (°C)
* Humidity (%)

## Running the Scripts:

1. Install Dependencies:
   
   Ensure you have the necessary Python libraries installed to run the scripts. You can install them using
   
        pip install requirements.txt


2. Run the [interface_sensor_2.py](./interface_sensor_2.py) 
3. Run the [interface_sensor_3.py](./interface_sensor_3.py)

## Accessing Environmental Data:

The **'sensirion_data'** variable within the scripts [interface_sensor_2.py](./interface_sensor_2.py) and the [interface_sensor_3.py](./interface_sensor_3.py) stores a dictionary containing the acquired sensor data. Here's an example structure:

    
    {'co2': 1166, 'temp': 33, 'hum': 38}
    {'co2': 1093, 'temp': 33, 'hum': 38}

Each key-value pair represents an environmental parameter:

* co2: CO2 concentration (ppm)
* temp: Temperature (°C)
* hum: Humidity (%)

## Modifying Scanning Sensor Data Frame Period

The [the sensirion.py](./sensirion.py)  script defines a variable named SCAN_SENSOR_PERIOD (in seconds) that controls the data acquisition interval. You can modify this value directly in the script to adjust the scanning frequency.

    SCAN_SENSOR_PERIOD = 10  #Default value (10 seconds)

      