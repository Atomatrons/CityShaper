#!/usr/bin/env micropython
import Robot
import My_block
import random
from time import sleep

Robot.gyro.compass_point = 0

Target_Angle = 120
for spins in range(0,10):
	My_block.spin_turn(Target_Angle)
	Target_Angle = Target_Angle + random.randint(-180,180)
	sleep(1)

	

