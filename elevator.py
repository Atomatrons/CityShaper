#!/usr/bin/env micropython 
import Robot

import My_block

Robot.tank_pair.on_for_rotations(50, 50, 2.9)
Robot.left_attachment.on_for_rotations(35, 0.25)
Robot.tank_pair.on_for_rotations(50, 50, -2.75)
Robot.tank_pair.on_for_rotations(50, 0, 0.025)
Robot.tank_pair.on_for_rotations(50, 50, -2.9)
