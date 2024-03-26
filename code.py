import time
import board
import pwmio
from adafruit_motor import servo

from adafruit_motor import motor #imports a small section of the adafruit_motor library

# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.GP0, duty_cycle=2 ** 15, frequency=50)
pwm1 = pwmio.PWMOut(board.GP1, duty_cycle=2 ** 15, frequency=50)


# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)
my_servo_1 = servo.Servo(pwm1)

while True:
    my_servo.angle = 0
    my_servo_1.angle = 0
    time.sleep(2)
    my_servo.angle = 180
    my_servo_1.angle = 180
    time.sleep(2)

'''
    for angle in range(0, 180, 5):
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -5):
        my_servo.angle = angle
        time.sleep(0.05)
'''
