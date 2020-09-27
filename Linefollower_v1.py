#!/usr/bin/env python3
import time
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_A, MoveSteering
from ev3dev2.sensor.lego import ColorSensor

right_motor = LargeMotor(OUTPUT_A)
left_motor = LargeMotor(OUTPUT_B)
steer_pair = MoveSteering(OUTPUT_A, OUTPUT_B, motor_class=LargeMotor)
time=0.03
count=0

cl = ColorSensor()
last_move=''
while True:
    color=cl.color_name
    print(color)
    if (color!="Black"):
        if (last_move=='right' or last_move==''):
            if (count>2):
                left_motor.on_for_seconds(speed=40, seconds=time*(count+1))
            else:
                left_motor.on_for_seconds(speed=40, seconds=time)
            last_move='left'
            count+=1
        if (last_move=='left'):
            if (count>2):
                right_motor.on_for_seconds(speed=40, seconds=time*(count+1))
            else:
                right_motor.on_for_seconds(speed=40, seconds=time)
            right_motor.on_for_seconds(speed=40, seconds=time)
            last_move='right'
            count+=1
    if(color=='Black'):
        steer_pair.on_for_seconds(steering=0, speed=50, seconds=time)
        count=0
    # else:
    #     steer_pair.on_for_seconds(steering=0, speed=50, seconds=time)
