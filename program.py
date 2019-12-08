#!/usr/bin/env micropython
import Robot
import My_block
def crane_and_blocks():
    Robot.gyro.compass_point = 0

    My_block.gyro_straight(30, 2.4)

    My_block.gyro_straight(-50, 1.1)

    My_block.spin_turn(90)

    Robot.sleep(0.1)

    My_block.gyro_straight(20, 0.93)
    
    My_block.spin_turn(0)

    Robot.sleep(0.1)

    My_block.gyro_straight(20,2.4)

    My_block.wall_square(-100)