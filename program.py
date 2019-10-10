#!/usr/bin/env micropython

import Robot
import my_block
from shiva_gyro import ShivaGyro

gyro = ShivaGyro(Robot, INPUT_2)

gyro.compass_point = 41

print(gyro.compass_point)