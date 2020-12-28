import time
import board
import busio

# Requires library, install with this command "pip3 install adafruit-circuitpython-si7021"
import adafruit_si7021

# start the fan
from gpiozero import LED

 
# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_si7021.SI7021(i2c)
 
 
while True:
        print("\nTemperature: %0.1f C" % sensor.temperature)
        print("Humidity: %0.1f %%" % sensor.relative_humidity)
        time.sleep(5)
        try:
                if(sensor.temperature > 25):
                        fan = LED(21)
                        print("hot",sensor.temperature)
                else:
                        fan.close()
                        print("cold", sensor.temperature)
        except:
                print("Error occured--")
