from enum import Enum

from gpiozero import PWMOutputDevice


class Pins(Enum):
    FORWARD_LEFT = 26
    FORWARD_RIGHT = 13
    REVERSE_LEFT = 19
    REVERSE_RIGHT = 6


pwm_forward_left = PWMOutputDevice(Pins.FORWARD_LEFT.value, True, 0, 1000)
pwm_reverse_left = PWMOutputDevice(Pins.REVERSE_LEFT.value, True, 0, 1000)

pwm_forward_right = PWMOutputDevice(Pins.FORWARD_RIGHT.value, True, 0, 1000)
pwm_reverse_right = PWMOutputDevice(Pins.REVERSE_RIGHT.value, True, 0, 1000)


def stop():
    pwm_forward_left.value = 0
    pwm_reverse_left.value = 0
    pwm_forward_right.value = 0
    pwm_reverse_right.value = 0


def forward():
    pwm_forward_left.value = 1
    pwm_reverse_left.value = 0
    pwm_forward_right.value = 1
    pwm_reverse_right.value = 0


def reverse():
    pwm_forward_left.value = 0
    pwm_reverse_left.value = 1
    pwm_forward_right.value = 0
    pwm_reverse_right.value = 1


def left():
    pwm_forward_left.value = 0
    pwm_reverse_left.value = 0
    pwm_forward_right.value = 1
    pwm_reverse_right.value = 0


def right():
    pwm_forward_left.value = 1
    pwm_reverse_left.value = 0
    pwm_forward_right.value = 0
    pwm_reverse_right.value = 0


# TODO: https://www.bluetin.io/python/gpio-pwm-raspberry-pi-h-bridge-dc-motor-control/
