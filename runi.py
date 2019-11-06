#!/usr/bin/env micropython

import Robot
<<<<<<< HEAD
"""This is mission 12 and 13 and it scores 95 points. This is Kyan and Rushil's mission.
"""

#Robot.gyro.compass_point = 0
Robot.tank_pair.on_for_rotations(50, 50, 4.5)
Robot.tank_pair.on_for_rotations(50, 50, -2.25)
Robot.tank_pair.on_for_rotations(0, 100, 3)
Robot.tank_pair.on_for_rotations(50, 50, 5)
=======
import My_block 
#Robot.gyro.compass_point = 0
Robot.tank_pair.on_for_rotations(50, 50, 2.25)
Robot.tank_pair.on_for_rotations(50, 50, -1)
My_block.spin_turn(200) 
Robot.tank_pair.on_for_rotations(50, 50, 2)
>>>>>>> 509a97a181a910f2025f666940fc78c82045fa41
