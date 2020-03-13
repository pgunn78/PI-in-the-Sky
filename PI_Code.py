import Adafruit_LSM303
import Adafruit_GPIO.SPI as SPI
import time
import RPi.GPIO as GPIO
import pigpio
from time import sleep
#the Pi stuff below is how we get a smooth servo turn
#it just makes the pi send smother infromation waves
pi = pigpio.pi()
pi.set_mode(17, pigpio.OUTPUT)
pi.set_PWM_frequency(17,50)
sleep(1)
print(pi.get_PWM_frequency(17))

lsm303 = Adafruit_LSM303.LSM303()


accel, mag = lsm303.read()
accel_x, accel_y, accel_z = accel
mag_x, mag_y, mag_z = mag
angle = mag_x

while True:
    # Read the X, Y, Z axis acceleration values and print them. accel is the acceleration mag is the direction/angle
    accel, mag = lsm303.read()
    # Grab the X, Y, Z components from the reading and print them out.
    accel_x, accel_y, accel_z = accel
    mag_x, mag_y, mag_z = mag

    if mag_x > angle:
        pi.set_servo_pulsewidth(17,500)
        sleep(1)
        pi.set_servo_pulsewidth(17,2500)
        sleep(1)


    print('Mag X={0}, Mag Y={1}, Mag Z={2}'.format(
        mag_x, mag_y, mag_z))
    time.sleep(1)