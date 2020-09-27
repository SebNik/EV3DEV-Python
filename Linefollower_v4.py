#!/usr/bin/env python3
import time
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_A, MoveSteering
from ev3dev2.sensor.lego import ColorSensor
import random

right_motor = LargeMotor(OUTPUT_A)
left_motor = LargeMotor(OUTPUT_B)
steer_pair = MoveSteering(OUTPUT_A, OUTPUT_B, motor_class=LargeMotor)
time=0.03

cl = ColorSensor()
last_move=''
while True:
    color=cl.color_name
    print(color)
    if (color!="Black"):
        if (last_move==''):
            if (random.randint(1,3)==1):
                last_move=='right'
            else:
                last_move='left'
        if (last_move=='right'):
            right_motor.on_for_seconds(speed=-40, seconds=time*1.5)
            left_motor.on_for_seconds(speed=40, seconds=time*2)
            last_move='left'
        if (last_move=='left'):
            left_motor.on_for_seconds(speed=-40, seconds=time*1.5)
            right_motor.on_for_seconds(speed=40, seconds=time*2)
            last_move='right'
    else :
        steer_pair.on_for_seconds(steering=0, speed=50, seconds=time)
        last_move=''
    # else:
    #     steer_pair.on_for_seconds(steering=0, speed=50, seconds=time)
