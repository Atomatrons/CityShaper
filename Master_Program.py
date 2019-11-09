#!/usr/bin/env micropython

import My_block
import Robot

# Checks if certain buttons are being pressed
while True:
    if Robot.button.up == True:
        Robot.sound.tone([(500, 350, 50)])
        for int in range(0, 1400):
            if Robot.button.enter == True:
                print("RUN 1 RUN 1 RUN 1 RUN 1 RUN 1 RUN 1 RUN 1")

    if Robot.button.down == True:
        Robot.sound.tone([(500, 350, 50), (500, 350, 50)])
        for int in range(0, 1400):
            if Robot.button.enter == True:
                print("RUN 2 RUN 2 RUN 2 RUN 2 RUN 2 RUN 2 RUN 2")

    if Robot.button.left == True:
        Robot.sound.tone([(500, 350, 50), (500, 350, 50), (500, 350, 50)])
        for int in range(0, 1400):
            if Robot.button.enter == True:
                print("RUN 3 RUN 3 RUN 3 RUN 3 RUN 3 RUN 3 RUN 3")

    if Robot.button.right == True:
        Robot.sound.tone([(500, 350, 50), (500, 350, 50), (500, 350, 50), (500, 350, 50)])
        for int in range(0, 1400):
            if Robot.button.enter == True:
                print("RUN 4 RUN 4 RUN 4 RUN 4 RUN 4 RUN 4 RUN 4")