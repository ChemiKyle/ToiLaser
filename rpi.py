#!/usr/bin/env python3

from time import sleep
from gpiozero import LED, MotionSensor
from db_interface import *

# Initialize objects for I/O devices, assign GPIO pins
laser = LED(17)
pir = MotionSensor(4)

while True:
    # Note: pir.wait_for_motion() causes program to become unexitable
    if pir.motion_detected:
        add_timestamp(conn, location_id)
        laser.on()
        sleep(5*60)
    else:
        laser.off()
