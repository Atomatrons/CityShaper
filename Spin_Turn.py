#!/usr/bin/env micropython
from shiva_gyro import ShivaGyro
import Robot
from sys import stderr

gyro = ShivaGyro(Robot.GYROSENSOR_PORT)

gyro.compass_point = 90

while True:
    print(gyro.compass_point, file=stderr)
