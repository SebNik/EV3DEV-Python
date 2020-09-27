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

while True:
    color=cl.color_name
    print(color)
    if (color!="Black"):
        for i in range(0,100):
            right_motor.on_for_seconds(speed=-40, seconds=time*2)
            left_motor.on_for_seconds(speed=40, seconds=time*2)
            if (cl.color_name=='Black'):
                break
            right_motor.on_for_seconds(speed=40, seconds=time*4)
            left_motor.on_for_seconds(speed=-40, seconds=time*4)
    else:
        steer_pair.on_for_seconds(steering=0, speed=50, seconds=time)
        last_move=''
    # else:
    #     steer_pair.on_for_seconds(steering=0, speed=50, seconds=time)
