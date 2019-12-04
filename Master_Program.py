#!/usr/bin/env micropython

# Master_Program: activates our programs based on different button combinations

import My_block
import Robot
from runi2 import push_block_return
from runi import push_tan_blocks_and_return

#Tells the runners that the program is ready to run
print("READY READY READY READY READY READY READY READY")
Robot.sound.tone([(900, 500, 100)], play_type=1)

# Checks if certain buttons are being pressed
while True:
    Robot.console.reset_console
    print("READY READY READY READY READY READY READY READY")
    
    if Robot.button.up == True:
        print("RUN 1 RUN 1 RUN 1 RUN 1 RUN 1 RUN 1 RUN 1")
        Robot.sound.tone([(500, 350, 50)], play_type=1)
        for int in range(0, 1400):
            if Robot.button.enter == True:
                print("RUN 1 RUN 1 RUN 1 RUN 1 RUN 1 RUN 1 RUN 1")
                Robot.sleep(0.2)
                Robot.console.reset_console()
                print("READY READY READY READY READY READY READY READY")
                Robot.sound.tone([(900, 500, 100)], play_type=1)   

    if Robot.button.down == True:
        print("RUN 2 RUN 2 RUN 2 RUN 2 RUN 2 RUN 2 RUN 2")
        Robot.sound.tone([(500, 350, 50), (500, 350, 50)], play_type=1)
        for int in range(0, 1400):
            if Robot.button.enter == True:
                print("RUN 2 RUN 2 RUN 2 RUN 2 RUN 2 RUN 2 RUN 2")
                Robot.sleep(0.2)
                Robot.console.reset_console()
                print("READY READY READY READY READY READY READY READY")
                Robot.sound.tone([(900, 500, 100)], play_type=1)

    if Robot.button.left == True:
        print("RUN 3 RUN 3 RUN 3 RUN 3 RUN 3 RUN 3 RUN 3")
        Robot.sound.tone([(500, 350, 50), (500, 350, 50), (500, 350, 50)], play_type=1)
        for int in range(0, 1400):
            if Robot.button.enter == True:
                print("RUN 3 RUN 3 RUN 3 RUN 3 RUN 3 RUN 3 RUN 3")
                Robot.sleep(0.2)
                push_tan_blocks_and_return()
                Robot.console.reset_console()
                print("READY READY READY READY READY READY READY READY")
                Robot.sound.tone([(900, 500, 100)], play_type=1)

    if Robot.button.right == True:
        print("RUN 4 RUN 4 RUN 4 RUN 4 RUN 4 RUN 4 RUN 4")
        Robot.sound.tone([(500, 350, 50), (500, 350, 50), (500, 350, 50), (500, 350, 50)], play_type=1)
        for int in range(0, 1400):
            if Robot.button.enter == True:
                print("RUN 4 RUN 4 RUN 4 RUN 4 RUN 4 RUN 4 RUN 4")
                Robot.sleep(0.2)
                push_block_return()
                Robot.console.reset_console()
                print("READY READY READY READY READY READY READY READY")
                Robot.sound.tone([(900, 500, 100)], play_type=1)