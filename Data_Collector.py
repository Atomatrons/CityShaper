#!/usr/bin/env micropython
import Robot
import My_block
import random
from time import sleep

Robot.gyro.compass_point = 0

# Test bounceback
Robot.log("My_block.spin_turn");
Target_Angle = 120
for spins in range(0, 3):
	My_block.spin_turn(Target_Angle)
	Target_Angle = Target_Angle + random.randint(-180,180)
	sleep(1)

# Test simple turn
Robot.log("My_block.simple_turn");
Target_Angle = 120
for spins in range(0, 3):
	My_block.simple_turn(Target_Angle)
	Target_Angle = Target_Angle + random.randint(-180,180)
	sleep(1)

# Test proportional turn
Robot.log("My_block.proportional");
Target_Angle = 120
for spins in range(0, 3):
	My_block.proportional(Target_Angle)
	Target_Angle = Target_Angle + random.randint(-180,180)
	sleep(1)
