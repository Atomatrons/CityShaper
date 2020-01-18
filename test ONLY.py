#!/usr/bin/env micropython 

from Swingset import swingset_mission
import My_block
import Robot

Robot.gyro.compass_point = 0

My_block.simple_turn(90)