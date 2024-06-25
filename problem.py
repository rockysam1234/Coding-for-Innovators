import time
import random

# Constants for soil moisture threshold and wait time
SOIL_MOISTURE_THRESHOLD = 30.0  # Soil moisture threshold in percentage
WAIT_TIME = 10  # Wait time in seconds

# Simulate the state of the irrigation system
irrigation_system_on = False

def read_soil_moisture():
    # Simulate reading soil moisture from a sensor
    return random.uniform(10.0, 50.0)

def activate_irrigation_system():
    global irrigation_system_on
    if not irrigation_system_on:
        print("Irrigation system ACTIVATED")
        irrigation_system_on = True

def deactivate_irrigation_system():
    global irrigation_system_on
    if irrigation_system_on:
        print("Irrigation system DEACTIVATED")
        irrigation_system_on = False

# Main loop
while True:
    # Read the current soil moisture level
    current_soil_moisture = read_soil_moisture()
    print(f"Current soil moisture: {current_soil_moisture:.2f}%")
    
    # Check soil moisture level and control irrigation system
    if current_soil_moisture < SOIL_MOISTURE_THRESHOLD:
        activate_irrigation_system()
    else:
        deactivate_irrigation_system()
    
    # Wait for a short period before the next reading
    time.sleep(WAIT_TIME)
