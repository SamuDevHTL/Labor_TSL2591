import board
import busio
from adafruit_tsl2591 import TSL2591

# Initialize I2C bus and TSL2591 sensor
i2c = busio.I2C(board.SCL, board.SDA)
sensor = TSL2591(i2c)

# Read and print each light measurement
print("Reading TSL2591 sensor data...")

# 1. Gesamthelligkeit (Total Brightness)
brightness = sensor.lux
print(f"Gesamthelligkeit (Total Brightness): {brightness} lux")

# 2. Infrarotlicht (Infrared Light)
infrared = sensor.infrared
print(f"Infrarotlicht (Infrared Light): {infrared}")

# 3. Sichtbares Licht (Visible Light)
# Visible light can be calculated as total spectrum - infrared
visible_light = sensor.visible
print(f"Sichtbares Licht (Visible Light): {visible_light}")

# 4. Gesamtspektrum (Full Spectrum)
full_spectrum = sensor.full_spectrum
print(f"Gesamtspektrum (Full Spectrum - IR + Visible Light): {full_spectrum}")
