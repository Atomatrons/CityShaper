#!/usr/bin/env micropython 

from Swingset import swingset_mission
import My_block
import Robot

Robot.gyro.compass_point = 0

My_block.gyro_straight(20, 0.75)


while True:
    My_block.spin_turn(90)
    Robot.sleep(0.3)
    My_block.spin_turn(0)

