#!/usr/bin/env micropython 

from Swingset import swingset_mission
import My_block
import Robot

Robot.gyro.compass_point = 0

swingset_mission()