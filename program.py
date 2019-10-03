#!/usr/bin/env micropython

import Robot

import My_block

My_block.line_square(-30, -30)

Robot.right_attachment.on_for_seconds(100, 5)

Robot.right_attachment.on_for_seconds(-100, 5)
