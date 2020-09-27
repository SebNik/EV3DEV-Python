#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B

large_motor = LargeMotor(OUTPUT_B)

#large_motor.on(speed=50)
large_motor.on_for_seconds(speed=40, seconds=3)
large_motor.wait_until_not_moving()
