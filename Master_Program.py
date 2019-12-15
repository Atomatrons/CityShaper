#!/usr/bin/env micropython

import My_block
import Robot
from runi2 import push_block_return
from runi import push_tan_blocks_and_return
from Anti_Drift_Thing import Anti_Drift_Thing

# Runs the gyro drift check program
Anti_Drift_Thing()

# Checks if certain buttons are being pressed
while True:
    if Robot.button.up == True:
        Robot.sound.tone([(500, 350, 50)])
        for int in range(0, 1400):
            if Robot.button.enter == True:
                Robot.sleep(0.2)
                print("RUN 1 RUN 1 RUN 1 RUN 1 RUN 1 RUN 1 RUN 1")

    if Robot.button.down == True:
        Robot.sound.tone([(500, 350, 50), (500, 350, 50)])
        for int in range(0, 1400):
            if Robot.button.enter == True:
                Robot.sleep(0.2)
                print("RUN 2 RUN 2 RUN 2 RUN 2 RUN 2 RUN 2 RUN 2")

    if Robot.button.left == True:
        Robot.sound.tone([(500, 350, 50), (500, 350, 50), (500, 350, 50)])
        for int in range(0, 1400):
            if Robot.button.enter == True:
                Robot.sleep(0.2)
                print("RUN 3 RUN 3 RUN 3 RUN 3 RUN 3 RUN 3 RUN 3")
                push_tan_blocks_and_return()

    if Robot.button.right == True:
        Robot.sound.tone([(500, 350, 50), (500, 350, 50), (500, 350, 50), (500, 350, 50)])
        for int in range(0, 1400):
            if Robot.button.enter == True:
                Robot.sleep(0.2)
                print("RUN 4 RUN 4 RUN 4 RUN 4 RUN 4 RUN 4 RUN 4")
                push_block_return()
