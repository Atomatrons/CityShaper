# Robot.py - Logical defenition of the robot with defnition of the ports on the EV3 and the sensors / motors connected to it

# Copyright of Viperbots FLL team  http://sites.google.com/view/viperbotsofficial/
# Can be freely used by any developors as long as you inform us on ViperbotsWHMS@gmail.com

# Modified by Shiva Atomatrons under the Viperbots licensing terms
from ev3dev2.console import Console
from time import sleep
import sys

# import motor modules and the ev3 ports used for it
from ev3dev2.motor import LargeMotor, Motor, OUTPUT_B, OUTPUT_C
from ev3dev2.motor import MoveSteering, MoveTank
from ev3dev2.motor import SpeedNativeUnits
from ev3dev2.motor import MediumMotor, OUTPUT_A, OUTPUT_D

# import Sensor modules and the ev3 ports used for it
from ShivaColor import ShivaColor
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_4

from ev3dev2.sensor.lego import GyroSensor, TouchSensor
from ev3dev2.sensor import INPUT_3
from ShivaGyro import ShivaGyro


# Port assignments
MEDIUM_MOTOR_LEFT = OUTPUT_A
MEDIUM_MOTOR_RIGHT = OUTPUT_D
LARGE_MOTOR_LEFT_PORT = OUTPUT_C
LARGE_MOTOR_RIGHT_PORT = OUTPUT_B


COLORSENSOR_RIGHT = INPUT_1
COLORSENSOR_LEFT = INPUT_3
TOUCHSENSOR_PORT = INPUT_4
GYROSENSOR_PORT = INPUT_2

# Attachment motor direction
CLK_WISE = 'clock_wise'  # positive speed
ANTI_CLK_WISE = 'anti_clck_wise'  # negative speed


# Create objects for the ev3 motors and sensors. Only one object will be created for each physical object and used in every program

# LARGEMOTORS USED FOR WHEELS
# Create individual wheel objects
left_wheel = Motor(LARGE_MOTOR_LEFT_PORT)
right_wheel = Motor(LARGE_MOTOR_RIGHT_PORT)

# Create object functions for basic movements for wheel pair blocks
steer_pair = MoveSteering(LARGE_MOTOR_LEFT_PORT, LARGE_MOTOR_RIGHT_PORT)
steer_pair.set_polarity(LargeMotor.POLARITY_INVERSED)

tank_pair = MoveTank(LARGE_MOTOR_LEFT_PORT, LARGE_MOTOR_RIGHT_PORT)
tank_pair.set_polarity(LargeMotor.POLARITY_INVERSED)

# MEDIUM MOTORS USED FOR ATTACHMENT GEARS
# Create individual motor objects
left_attachment = MediumMotor(MEDIUM_MOTOR_LEFT)
right_attachment = MediumMotor(MEDIUM_MOTOR_RIGHT)


# Create Color sensor objects

right_color = ShivaColor(COLORSENSOR_RIGHT)
left_color = ShivaColor(COLORSENSOR_LEFT)

# Create GYROSENSOR
gyro = ShivaGyro(GYROSENSOR_PORT)
gyro.mode = ShivaGyro.MODE_GYRO_ANG

# Create Touch
touch = TouchSensor(TOUCHSENSOR_PORT)

# Sets the font size for robot lcd
console = Console()
console.set_font('Lat15-VGA16.psf.gz')

# Debug print code


def debug_print(*args, **kwargs):
    '''Print debug messages to stderr.
    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=sys.stderr)


log_file = open('log.txt', 'w+')


def log(*args, **kwargs):
    '''Print debug messages to stderr.
    This shows up in the output panel in VS Code.
    '''
    print(*args, **kwargs, file=log_file)
