#!/usr/bin/env micropython
import Robot
import My_block
from sys import stderr

Robot.gyro.compass_point = 0

My_block.SpinTurn(90)

My_block.SpinTurn(0)
