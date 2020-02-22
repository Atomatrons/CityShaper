 #!/usr/bin/env micropython

# Drone: Completes M-03 Inspection Drone.

import Robot
import My_block


def drone():
    """ Innovative Architecture and Bat missions
       Completes M-03 Inspection Drone, plus the
    """

    # Establishes the compass point the robot is facing
    Robot.gyro.compass_point = 0

    # Moves the robot forward, turns, and pushes architecture to circle
    My_block.gyro_straight(35,1)
    My_block.spin_turn(44)
    My_block.gyro_straight(35, 1.7)

    # backs up
    My_block.gyro_straight(35,-1.7)

    #turns to drone
    My_block.spin_turn(0)
    return


drone()