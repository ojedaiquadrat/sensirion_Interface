"""
This file defines constants and variables used throughout the script.
"""

global connected
global raw_sensor_dataframe

# Define constants using all uppercase characters with underscores for separation
MAX_RETRIES = 5  # Maximum number of retries for connecting to the sensor
SCAN_SENSOR_PERIOD = 10.0  # Scanning sensor data frame period in seconds
LOG_LEVEL = "INFO"  # Logging level (e.g., DEBUG, INFO, WARNING, ERROR)

# Define variables with descriptive names and potential initial values
connected = False  # Flag to indicate sensor connection status
topic_name = "sensirion_1"  # Kafka topic name for sensor data
sensor_mac_address = "E1:BE:94:7B:0D:70"  # Sensor's MAC address (replace with actual address)
raw_sensor_dataframe = []

# Service UUIDs for the BLE sensor (replace with actual values if different)
SERVICE_UUID_LOGGING_INTERVAL = "00008001-B38D-4985-720E-0F993A68EE41"
SERVICE_UUID_AVAILABLE_SAMPLES = "00008002-B38D-4985-720E-0F993A68EE41"
SERVICE_UUID_REQUESTED_SAMPLES = "00008003-B38D-4985-720E-0F993A68EE41"
SERVICE_UUID_DATA_TRANSFER = "00008004-B38D-4985-720E-0F993A68EE41"

