#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import random


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
#ev3.speaker.beep()

# Initialize a motor at port A & D
left_motor = Motor(Port.D)
right_motor = Motor(Port.A)

# Initialize sensors
left_sensor = ColorSensor(Port.S1)
right_sensor = ColorSensor(Port.S4)
middle_sensor = ColorSensor(Port.S3)

# Initialize drive base
robot = DriveBase(left_motor, right_motor, wheel_diameter=442, axle_track=1600)

BLACK = 5
GRAY = 80
threshold = (BLACK + GRAY) / 2 # 42.5
soft_threshold = threshold / 2 # 21.25

DRIVE_SPEED = 1000

PROPORTIONAL_GAIN = 1.2

# Constants for correction behavior
CORRECTION_DURATION = 500  # Time in milliseconds
CORRECTION_SPEED = 300     # Speed for correction

MAP = [
    [2, 1, 1, 2],
    [1, 0, 0, 1],
    [1, 0, 0, 1],
    [2, 1, 1, 2]
]
# 0: Middle
# 1: Edge
# 2: Corner
# GOAL: Diamond to [3, 3]
GOAL = [3, 3]

class State:
    def __init__(self, a, b):
        self.car = [0, 0]
        self.diamond = [1, 1]

    def successor():
        self.successor_states = [] # Forward, right, left, backwards
        


BEHAVIORS = []

while DIAMOND != GOAL:
    # Read sensor values
    left_reflection = left_sensor.reflection()
    right_reflection = right_sensor.reflection()
    middle_reflection = middle_sensor.reflection()

    # Determine the state based on sensor readings
    if middle_reflection < threshold:
        robot.drive(DRIVE_SPEED, 0)
    else:
        robot.stop()

        if left_reflection < threshold:
            robot.turn(90)
