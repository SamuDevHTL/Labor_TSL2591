import time
import csv
import board
import busio
from datetime import datetime
from adafruit_tsl2591 import TSL2591

# Initialize I2C bus and TSL2591 sensor
i2c = busio.I2C(board.SCL, board.SDA)
sensor = TSL2591(i2c)

# Define the CSV file path
csv_file_path = "tsl2591_data.csv"

# Set allowed range for sensor values
MIN_VALUE = 0
MAX_VALUE = 100000  # Adjust based on real-world conditions

# Function to log data to CSV
def log_to_csv(data):
    with open(csv_file_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(data)

# Initialize CSV file with headers
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Total Brightness (lux)", "Infrared Light", "Visible Light", "Full Spectrum"])

# Start reading and logging sensor data
try:
    while True:
        try:
            # Read sensor values
            brightness = sensor.lux
            infrared = sensor.infrared
            visible_light = sensor.visible
            full_spectrum = sensor.full_spectrum

            # Debugging: Print raw sensor values
            print(f"DEBUG - Brightness: {brightness}, Infrared: {infrared}, Visible Light: {visible_light}, Full Spectrum: {full_spectrum}")

            # Check if all values are within the allowed range
            if all(MIN_VALUE <= value <= MAX_VALUE for value in [brightness, infrared, visible_light, full_spectrum]):
                # Get the current timestamp
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Prepare data for CSV
                data = [timestamp, brightness, infrared, visible_light, full_spectrum]

                # Write data to CSV
                log_to_csv(data)
                print(f"Logged data at {timestamp}: {data}")
            else:
                # Log out-of-range values for debugging
                if not (MIN_VALUE <= brightness <= MAX_VALUE):
                    print(f"Brightness out of range: {brightness}")
                if not (MIN_VALUE <= infrared <= MAX_VALUE):
                    print(f"Infrared out of range: {infrared}")
                if not (MIN_VALUE <= visible_light <= MAX_VALUE):
                    print(f"Visible Light out of range: {visible_light}")
                if not (MIN_VALUE <= full_spectrum <= MAX_VALUE):
                    print(f"Full Spectrum out of range: {full_spectrum}")
                print("Sensor values out of range, data not logged.")

        except Exception as e:
            # Handle any errors that occur during sensor reading
            print(f"Error reading sensor data: {e}")

        # Wait for 1 second before the next reading
        time.sleep(1)

except KeyboardInterrupt:
    # Graceful exit on Ctrl+C
    print("Data logging stopped.")
