from enum import Enum

from gpiozero import PWMOutputDevice


class Pins(Enum):
    FORWARD_LEFT = 18
    FORWARD_RIGHT = 27
    REVERSE_LEFT = 24
    REVERSE_RIGHT = 10


class Speed(Enum):
    NONE = 0.
    LOW = 0.2
    HIGH = 0.8
    FULL = 1.0


pwm_forward_left = PWMOutputDevice(Pins.FORWARD_LEFT.value, True, 0, 1000)
pwm_reverse_left = PWMOutputDevice(Pins.REVERSE_LEFT.value, True, 0, 1000)

pwm_forward_right = PWMOutputDevice(Pins.FORWARD_RIGHT.value, True, 0, 1000)
pwm_reverse_right = PWMOutputDevice(Pins.REVERSE_RIGHT.value, True, 0, 1000)


def stop():
    """Stop all motion"""
    pwm_forward_left.value = Speed.NONE.value
    pwm_reverse_left.value = Speed.NONE.value
    pwm_forward_right.value = Speed.NONE.value
    pwm_reverse_right.value = Speed.NONE.value


def forward():
    """Go forwards"""
    pwm_forward_left.value = Speed.FULL.value
    pwm_reverse_left.value = Speed.NONE.value
    pwm_forward_right.value = Speed.FULL.value
    pwm_reverse_right.value = Speed.NONE.value


def reverse():
    """Go backwards"""
    pwm_forward_left.value = Speed.NONE.value
    pwm_reverse_left.value = Speed.FULL.value
    pwm_forward_right.value = Speed.NONE.value
    pwm_reverse_right.value = Speed.FULL.value


def left():
    """Spin the car left"""
    pwm_forward_left.value = Speed.NONE.value
    pwm_reverse_left.value = Speed.FULL.value
    pwm_forward_right.value = Speed.FULL.value
    pwm_reverse_right.value = Speed.NONE.value


def right():
    """Spin the car right"""
    pwm_forward_left.value = Speed.FULL.value
    pwm_reverse_left.value = Speed.NONE.value
    pwm_forward_right.value = Speed.NONE.value
    pwm_reverse_right.value = Speed.FULL.value


# TODO: https://www.bluetin.io/python/gpio-pwm-raspberry-pi-h-bridge-dc-motor-control/
