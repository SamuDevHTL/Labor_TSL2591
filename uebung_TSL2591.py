import board
import busio
from adafruit_tsl2591 import TSL2591
import csv
import time

# Initialize I2C bus and TSL2591 sensor
i2c = busio.I2C(board.SCL, board.SDA)
sensor = TSL2591(i2c)

# File to save the data
csv_file = "tsl2591_data.csv"

# Create and write the header row in the CSV file
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Total Brightness (lux)", "Infrared Light", "Visible Light", "Full Spectrum"])

print("Reading TSL2591 sensor data and saving to CSV file...")

# Continuous logging
try:
    while True:
        # Get the current timestamp
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        
        # Read sensor data
        brightness = sensor.lux
        infrared = sensor.infrared
        visible_light = sensor.visible
        full_spectrum = sensor.full_spectrum
        
        # Print the readings
        print(f"Timestamp: {timestamp}")
        print(f"Gesamthelligkeit (Total Brightness): {brightness} lux")
        print(f"Infrarotlicht (Infrared Light): {infrared}")
        print(f"Sichtbares Licht (Visible Light): {visible_light}")
        print(f"Gesamtspektrum (Full Spectrum - IR + Visible Light): {full_spectrum}")
        print("-" * 40)
        
        # Save the data to the CSV file
        with open(csv_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, brightness, infrared, visible_light, full_spectrum])
        
        # Wait for 5 seconds
        time.sleep(5)

except KeyboardInterrupt:
    print("\nData logging stopped.")
