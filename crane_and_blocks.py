#!/usr/bin/env micropython


def spin_turn_2(target_angle):
    """
    Turns the robot untill the gyro reads the target angle compass point
    """
    # Turns on the motors
    if target_angle > Robot.gyro.compass_point:
        Robot.tank_pair.on(20, -20)
    else:
        Robot.tank_pair.on(-20, 20)

    # Checks if the gyro compass point angle equals target_angle
    if target_angle > Robot.gyro.compass_point:
        while target_angle > Robot.gyro.compass_point:
            pass
        Robot.tank_pair.off(brake=True)

        # Precisely turns back to the desired angle if the robot overshot
        if target_angle < Robot.gyro.compass_point:
            while target_angle < Robot.gyro.compass_point:
                Robot.tank_pair.on(-2, 2)
    # Checks if the gyro compass point angle equals target_angle
    else:
        while target_angle < Robot.gyro.compass_point:
            pass
        Robot.tank_pair.off(brake=True)
        Robot.sleep(0.55)

        # Precisely turns back to the desired angle if the robot overshot
        if target_angle > Robot.gyro.compass_point:
            while target_angle > Robot.gyro.compass_point:
                Robot.tank_pair.on(2, -2)



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

    My_block.gyro_straight(-70, 0.9)

    # Alligns with the crane

    spin_turn_2(90)

    My_block.gyro_straight(25, 0.9)

    My_block.spin_turn(0)

    # Completes the crane mission

    My_block.gyro_straight(25, 2.05)

    Robot.sleep(0.3)

    My_block.gyro_straight(-10, 0.3)

    # Returns home

    My_block.wall_square(-100)

    My_block.gyro_straight(25, 0.2)

    My_block.spin_turn(-40)

    Robot.steer_pair.on_for_rotations(0, 100, 3.9)
