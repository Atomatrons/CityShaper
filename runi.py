#!/usr/bin/env micropython

import Robot
import My_block 
#Robot.gyro.compass_point = 0
Robot.tank_pair.on_for_rotations(50, 50, 2.25)
Robot.tank_pair.on_for_rotations(50, 50, -1)
My_block.spin_turn(200) 
Robot.tank_pair.on_for_rotations(50, 50, 2)
