# My_block.py - Utility functions for use in runs
import time
import Robot
import Shiva_Steering

# Defines the line square function
def line_square(left_wheel_speed=10, right_wheel_speed=10):
    """
    Program that squares to a line. 
    First parameter defines the left wheel speed, and the second one defines the right.
    """

    # Turns on the motors
    Robot.left_wheel.on(left_wheel_speed)
    Robot.right_wheel.on(right_wheel_speed)

    # Esablishes varibles that tell the program if a motor is stopped
    left_is_on = True
    right_is_on = True

    # Checks the color sensor values to find black. When a color sensor finds black, it stops the corresponding motor.

    while left_is_on or right_is_on == True:

        if Robot.right_color.is_at_white():
            Robot.right_wheel.off(brake=True)
            right_is_on = False

        if Robot.left_color.is_at_white():
            Robot.left_wheel.off(brake=True)
            left_is_on = False

    Robot.tank_pair.on(5, 5)

    left_is_on = True
    right_is_on = True

    while left_is_on or right_is_on == True:

        if Robot.right_color.is_at_black():
            Robot.right_wheel.off(brake=True)
            right_is_on = False

        if Robot.left_color.is_at_black():
            Robot.left_wheel.off(brake=True)
            left_is_on = False

# Defines the wall square function
def wall_square(speed=10):
    """
    Program that squares against a wall
    """
    # force robot to go backwards
    if speed > 0:
        speed = speed * (-1)
    # go to wall
    Robot.steer_pair.on(0, speed)
    while True:
        if Robot.touch.is_pressed == True:
            Robot.sleep(0.2)
            Robot.steer_pair.off(brake=True)
            break

# Do spin turn, using bounceback for accuracy
def spin_turn(target_angle):
    """
    Turns the robot untill the gyro reads the target angle compass point
    """
    start_time = time.time()
    start_angle = Robot.gyro.compass_point

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
        Robot.sleep(0.2)

        # Precisely turns back to the desired angle if the robot overshot
        if target_angle < Robot.gyro.compass_point:
            while target_angle < Robot.gyro.compass_point:
                Robot.tank_pair.on(-2, 2)
    # Checks if the gyro compass point angle equals target_angle
    else:
        while target_angle < Robot.gyro.compass_point:
            pass
        Robot.tank_pair.off(brake=True)
        Robot.sleep(0.2)

        # Precisely turns back to the desired angle if the robot overshot
        if target_angle > Robot.gyro.compass_point:
            while target_angle > Robot.gyro.compass_point:
                Robot.tank_pair.on(2, -2)

    # Log elapsed time, number of degrees turned, and accuracy of turn
    Robot.log("{},{},{}".format(
        time.time() - start_time,                       # elapsed time
        abs(start_angle - target_angle),                # degrees actually turned
        abs(target_angle - Robot.gyro.compass_point)    # error
        ))

# Do spin turn, using proportional speed control for accuracy
def proportional_turn(target_angle):
    '''
    proportional_turn goes from the compass point it's pointing at to the target angle with a slowly decreasing speed.  
    '''
    start_time = time.time()
    start_angle = Robot.gyro.compass_point

    current_angle = Robot.gyro.compass_point
    amplification = 0.5

    # clockwise
    if current_angle < target_angle:
        while current_angle < target_angle:
            speed = (target_angle - current_angle) * amplification
            if speed > 90:
                speed = 90
            if speed < 3:
                speed = 3
            Robot.tank_pair.on(speed, -speed)
            current_angle = Robot.gyro.compass_point
        
    # counterclockwise
    else:
        while current_angle > target_angle:
            speed = abs(target_angle - current_angle) * amplification
            if speed > 90:
                speed = 90
            if speed < 3:
                speed = 3
            Robot.tank_pair.on(-speed, speed)
            current_angle = Robot.gyro.compass_point

    # Log elapsed time, number of degrees turned, and accuracy of turn
    Robot.log("{},{},{}".format(
        time.time() - start_time,                       # elapsed time
        abs(start_angle - target_angle),                # degrees actually turned
        abs(target_angle - Robot.gyro.compass_point)    # error
        ))

# Do spin turn, with no correction for accuracy
def simple_turn(target_angle):
    """
    Turns the robot untill the gyro reads the target angle compass point
    """
    start_time = time.time()
    start_angle = Robot.gyro.compass_point

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
        Robot.sleep(0.2)

    # Checks if the gyro compass point angle equals target_angle
    else:
        while target_angle < Robot.gyro.compass_point:
            pass
        Robot.tank_pair.off(brake=True)
        Robot.sleep(0.2)

    # Log elapsed time, number of degrees turned, and accuracy of turn
    Robot.log("{},{},{}".format(
        time.time() - start_time,                       # elapsed time
        abs(start_angle - target_angle),                # degrees actually turned
        abs(target_angle - Robot.gyro.compass_point)    # error
        ))

# Defines the gyro_straight function
def gyro_straight(speed, rotations):
    """
    Makes the robot go straight using the gyro.
    """
    # Sets the degree value the robot will try to stick to
    start_heading = Robot.gyro.angle

    # checks if the robot should go backward or not
    if rotations*speed < 0:
        # backwards
        if rotations > 0:
            target_rotations = Robot.left_wheel.rotations - rotations
        else:
            target_rotations = Robot.left_wheel.rotations + rotations
            speed = speed * -1

        while Robot.left_wheel.rotations > target_rotations:
            Robot.steer_pair.on(Robot.gyro.angle - start_heading, -abs(speed))
    else:
        # forwards
        if rotations < 0:
            target_rotations = Robot.left_wheel.rotations - rotations
            speed = speed * -1
        else:
            target_rotations = Robot.left_wheel.rotations + rotations

        while Robot.left_wheel.rotations < target_rotations*Shiva_Steering.factor:
            Robot.steer_pair.on(start_heading-Robot.gyro.angle, speed)
    Robot.steer_pair.off(brake=True)

# Defines the ramp_gyro_straight function
def ramp_gyro_straight(start_speed, end_speed, rotations):
    """
    Makes the robot go straight using the gyro, changing speed from start_speed to end_speed.
    """
    # Sets the degree value the robot will try to stick to
    start_heading = Robot.gyro.angle

    # checks if the robot should go backward or not
    if rotations*start_speed < 0:
        # backwards
        if rotations > 0:
            target_rotations = Robot.left_wheel.rotations - rotations
        else:
            target_rotations = Robot.left_wheel.rotations + rotations
            speed = start_speed * -1

        while Robot.left_wheel.rotations > target_rotations:
            while start_speed < end_speed:
                Robot.steer_pair.on(
                    start_heading-Robot.gyro.angle, -abs(start_speed))
                start_speed = start_speed+0.7

            Robot.steer_pair.on(
                (Robot.gyro.angle-start_heading)*2, -abs(end_speed))
    else:
        # forwards
        if rotations < 0:
            target_rotations = Robot.left_wheel.rotations - rotations
            speed = speed * -1
        else:
            target_rotations = Robot.left_wheel.rotations + rotations

        while Robot.left_wheel.rotations < target_rotations*Shiva_Steering.factor:
            while start_speed < end_speed:
                Robot.steer_pair.on(
                    start_heading-Robot.gyro.angle, start_speed)
                start_speed = start_speed+0.7
            Robot.steer_pair.on((start_heading-Robot.gyro.angle)*2, end_speed)
    Robot.steer_pair.off(brake=True)

# Defines the ramp speed function
def ramp_speed(start_speed, end_speed, rotations):
    start_rotations = Robot.left_wheel.rotations
    end_rotations = start_rotations + rotations
    while Robot.left_wheel.rotations <=  end_rotations*Shiva_Steering.factor:
        while start_speed < end_speed:
            Robot.tank_pair.on(start_speed, start_speed)
            start_speed = start_speed+0.2
        Robot.tank_pair.on(end_speed, end_speed)

# Defines the line follower function
def line_follower(speed, rotations):

    while Robot.right_color.is_at_white == False:
        Robot.steer_pair.on(20, 15)

    Robot.left_wheel.reset

    while Robot.left_wheel.rotations < rotations:
        steering_factor = Robot.right_color.reflected_light_intensity-30
        Robot.steer_pair.on(steering_factor, speed)
