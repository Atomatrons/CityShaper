#!/usr/bin/env micropython
import Robot
from shiva_gyro import ShivaGyro
from sys import stderr
from Spin_Turn import spin_turn

Robot.gyro.compass_point = 90

spin_turn(180)
