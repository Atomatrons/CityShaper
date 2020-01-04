#!/usr/bin/env micropython
import Robot
import My_block

# Crane_and_blocks: Completes M-02 Crane, and M-12 Design and Build.


def crane_and_blocks():
    """
    Completes M-02 Crane, and M-12 Design and Build.
    """

    # Establishes the compass point the robot is facing

    Robot.gyro.compass_point = 0

    # Drops off the blocks in the circle

    My_block.gyro_straight(30, 2.2)

    My_block.gyro_straight(-50, 0.9)

    # Alligns with the crane

    My_block.spin_turn(90)

    My_block.gyro_straight(20, 0.83)

    My_block.spin_turn(0)

    # Completes the crane mission

    My_block.gyro_straight(10, 1.93)

    Robot.sleep(0.3)

    My_block.gyro_straight(-10, 0.3)

    # Returns home

    My_block.wall_square(-100)

    My_block.gyro_straight(20, 0.2)

    My_block.spin_turn(-40)

    Robot.steer_pair.on_for_rotations(0, 100, 3.9)
